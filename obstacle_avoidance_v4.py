import picar_4wd as fc
import time
import signal
import sys
from collections import deque

base_speed = 20
last_turn = None  # Memory for exploration direction
distance_history = deque(maxlen=5)  # Store last 5 front distances


# === Safe Stop ===
def stop_robot(signum=None, frame=None):
    print("\n Stopping robot safely")
    fc.stop()
    sys.exit(0)


# Register stop signals
signal.signal(signal.SIGINT, stop_robot)
signal.signal(signal.SIGTERM, stop_robot)
signal.signal(signal.SIGTSTP, stop_robot)


# === Curved Turn Logic ===
def curved_turn(direction, speed):
    if direction == "left":
        fc.set_motor_power(1, -int(speed / 2))
        fc.set_motor_power(2, speed)
        fc.set_motor_power(3, -int(speed / 2))
        fc.set_motor_power(4, speed)
    elif direction == "right":
        fc.set_motor_power(1, speed)
        fc.set_motor_power(2, -int(speed / 2))
        fc.set_motor_power(3, speed)
        fc.set_motor_power(4, -int(speed / 2))


# === Predictive Trajectory Check ===
def is_approaching(distances, min_drop=5):
    if len(distances) < 3:
        return False
    return all(
        distances[i] - distances[i + 1] >= min_drop
        for i in range(len(distances) - 1)
    )


# === Main Loop ===
def main():
    global last_turn
    print(" Mode: Predictive Obstacle Avoidance with Curved Turns")

    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        print(" Scan:", scan_list)
        distance = fc.get_distance_at(0)
        distance_history.append(distance)
        print(f" Front Distance: {distance} cm | History: {list(distance_history)}")

        # === Predictive Obstacle Detection ===
        if is_approaching(distance_history):
            print(" Predictive Collision Alert! Object approaching fast.")
            speed = 5
        elif distance < 20:
            speed = 5
        elif distance < 35:
            speed = 10
        else:
            speed = base_speed

        # === Surrounded Detection ===
        if scan_list.count(2) == 0:
            print(" Surrounded! Reversing...")
            fc.backward(speed)
            time.sleep(0.5)
            direction = "right" if last_turn == "left" else "left"
            print(f" Turning {direction} to escape")
            curved_turn(direction, speed)
            time.sleep(0.5)
            last_turn = direction
            continue

        # === Path Analysis ===
        left_free = scan_list[:5].count(2)
        right_free = scan_list[5:].count(2)

        if scan_list[3:7] != [2, 2, 2, 2]:  # Obstacle ahead
            if left_free > right_free:
                direction = "left"
            elif right_free > left_free:
                direction = "right"
            else:
                direction = "right" if last_turn == "left" else "left"
            print(f" Turning {direction}")
            curved_turn(direction, speed)
            last_turn = direction
        else:
            print(" Path clear — Moving forward")
            fc.forward(speed)

        time.sleep(0.15)


if __name__ == "__main__":
    main()
