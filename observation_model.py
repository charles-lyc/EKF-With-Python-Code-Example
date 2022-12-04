import numpy as np

# Author: Addison Sears-Collins
# https://automaticaddison.com
# Description: An observation model for a differential drive mobile robot

# Measurement matrix H_t
# Used to convert the predicted state estimate at time t
# into predicted sensor measurements at time t.
# In this case, H will be the identity matrix since the
# estimated state maps directly to state measurements from the
# odometry data [x, y, yaw]
# H has the same number of rows as sensor measurements
# and same number of columns as states.
H_t = np.array([[1.0,  0, 0],
                [0, 1.0,  0],
                [0,  0, 1.0]])

# Sensor noise. This is a vector with the
# number of elements equal to the number of sensor measurements.
sensor_noise_w_t = np.array([0, 0, 0])

# The estimated state vector at time t in the global
# reference frame
# [x_t, y_t, yaw_t]
# [meters, meters, radians]
state_estimate_t = np.array([5.2, 2.8, 1.5708])


def main():
    sensor_noise_w_t[0] = (np.random.rand()-0.5)*6
    sensor_noise_w_t[1] = (np.random.rand()-0.5)*6
    sensor_noise_w_t[2] = (np.random.rand()-0.5)*6

    estimated_sensor_observation_y_t = H_t @ state_estimate_t + sensor_noise_w_t

    print(f'State at time t: {state_estimate_t}')
    print(
        f'Estimated sensor observations at time t: {estimated_sensor_observation_y_t}')


main()
