import matplotlib.pyplot as plt
import numpy as np

# Author: Addison Sears-Collins
# https://automaticaddison.com
# Description: A state space model for a differential drive mobile robot

# A matrix
# 3x3 matrix -> number of states x number of states matrix
# Expresses how the state of the system [x,y,yaw] changes
# from t-1 to t when no control command is executed.
# Typically a robot on wheels only drives when the wheels are commanded
# to turn.
# For this case, A is the identity matrix.
# A is sometimes F in the literature.
A_t_minus_1 = np.array([[1.0,  0,   0],
                        [0, 1.0,   0],
                        [0,  0, 1.0]])

# The estimated state vector at time t-1 in the global
# reference frame
# [x_t_minus_1, y_t_minus_1, yaw_t_minus_1]
# [meters, meters, radians]
state_estimate_t = np.array([0.0, 0.0, 0.0])
state_estimate_t_minus_1 = np.array([0.0, 0.0, 0.0])

# The control input vector at time t-1 in the global
# reference frame
# [v, yaw_rate]
# [meters/second, radians/second]
# In the literature, this is commonly u.
control_vector_t_minus_1 = np.array([4.5, 0.01])

# Noise applied to the forward kinematics (calculation
# of the estimated state at time t from the state
# transition model of the mobile robot). This is a vector
# with the number of elements equal to the number of states
process_noise_v_t_minus_1 = np.array([0, 0, 0])

delta_t = 0.001  # seconds


def getB(yaw, dt):
    """
    Calculates and returns the B matrix
    3x2 matix -> number of states x number of control inputs
    The control inputs are the forward speed and the
    rotation rate around the z axis from the x-axis in the
    counterclockwise direction.
    [v, yaw_rate]
    Expresses how the state of the system [x,y,yaw] changes
    from t-1 to t due to the control commands (i.e. control
    input).
    :param yaw: The yaw (rotation angle around the z axis) in rad
    :param dt: The change in time from time step t-1 to t in sec
      """
    B = np.array([[np.cos(yaw)*dt, 0],
                  [np.sin(yaw)*dt, 0],
                  [0, dt]])

    return B


def main():

    # a = np.array([[1.0,  0],
    #               [1.0,  0],
    #               [0,  1.0]])
    # b = np.array([[7.7],
    #               [0]])

    # c = a@b
    # print(a)
    # print(b)
    # print(c)
    # return

    times = range(1000)
    for i in times:
        state_estimate_t = A_t_minus_1 @ state_estimate_t_minus_1 + \
            getB(state_estimate_t_minus_1[2], delta_t) @ control_vector_t_minus_1 + \
            process_noise_v_t_minus_1

        # sb??????????????????????????????????????????????????????????????????0???????????????????????????????????????dt
        # print("test")
        # print(A_t_minus_1)
        # print(state_estimate_t_minus_1)
        # print(A_t_minus_1 @ state_estimate_t_minus_1)
        # print(getB(0, delta_t))
        # print(control_vector_t_minus_1)
        # print(getB(0, delta_t)@control_vector_t_minus_1)
        # print("test over")

        # print(f'State at time t-1: {state_estimate_t_minus_1}')
        # print(f'Control input at time t-1: {control_vector_t_minus_1}')
        # print("process_noise_v_t_minus_1: ", process_noise_v_t_minus_1)
        # print(f'State at time t: {state_estimate_t}')

        plt.plot(state_estimate_t[0], state_estimate_t[1], 'ro')

        # iteration
        # print(state_estimate_t[0])
        # yaw_angle = state_estimate_t[2]
        state_estimate_t_minus_1[0] = state_estimate_t[0]
        state_estimate_t_minus_1[1] = state_estimate_t[1]
        state_estimate_t_minus_1[2] = state_estimate_t[2]
        process_noise_v_t_minus_1[0] = (np.random.rand()-0.5)*2
        process_noise_v_t_minus_1[1] = (np.random.rand()-0.5)*2
        process_noise_v_t_minus_1[2] = (np.random.rand()-0.5)*2.01

    # plt.ylabel('some numbers')
    plt.show()


main()
