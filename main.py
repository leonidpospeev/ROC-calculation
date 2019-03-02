#Tere!

import numpy as np
import matplotlib.pyplot as plt

NUM_POINTS = 500
MA_WINDOW = 100

measurement_error = 2


# Generating the values and ROCs for the case when the process formula is known
# and the ROC is known and remains constant
def generate_temperature_profile1():
    time = np.linspace(0, NUM_POINTS - 1, NUM_POINTS)

    k = 0.1

    true_value = k * time
    measured_value = true_value + measurement_error * np.random.randn(NUM_POINTS) / 3

    true_value_roc = k * np.ones(NUM_POINTS)
    measured_value_roc1 = np.zeros(NUM_POINTS)
    measured_value_roc2 = np.zeros(NUM_POINTS)
    for i in range(MA_WINDOW, NUM_POINTS):
        measured_value_roc1[i] = np.polyfit(time[i - MA_WINDOW:i], measured_value[i - MA_WINDOW:i], 1)[0]
        measured_value_roc2[i] = (measured_value[i-MA_WINDOW] - measured_value[i])/ (time[i-MA_WINDOW]-time[i])

    f, ax1 = plt.subplots()
    ax1.plot(time, true_value, label='true value')
    ax1.plot(time, measured_value, label='measured value')
    #ax1.plot(time, true_value_roc, label='true ROC')
    #ax1.plot(time, measured_value_roc2, label='simple ratio ROC')
    #ax1.plot(time, measured_value_roc1, label='linear fit ROC')
    ax1.legend()
    ax1.set_xlim(0, NUM_POINTS)
    #ax1.set_ylim(-0.2, 0.4)
    plt.show()


# Generating the values and ROCs for the case when the process formula is known
# and the ROC is known and does not remain constant
def generate_temperature_profile2():
    time = np.linspace(0, NUM_POINTS - 1, NUM_POINTS)

    T0 = 0
    Ts = 25
    k = 0.05

    true_value = Ts + (T0 - Ts) * np.exp(-k * time)
    measured_value = true_value + measurement_error * np.random.randn(NUM_POINTS) / 3

    true_value_roc = k * (Ts - T0) * np.exp(-k * time)
    measured_value_roc1 = np.zeros(NUM_POINTS)
    measured_value_roc2 = np.zeros(NUM_POINTS)
    for i in range(MA_WINDOW, NUM_POINTS):
        measured_value_roc1[i] = np.polyfit(time[i - MA_WINDOW:i], measured_value[i - MA_WINDOW:i], 1)[0]
        measured_value_roc2[i] = (measured_value[i-MA_WINDOW] - measured_value[i])/(time[i-MA_WINDOW]-time[i])

    f, ax1 = plt.subplots()
    ax1.plot(time, true_value, label='true value')
    ax1.plot(time, measured_value, label='measured value')
    #ax1.plot(time, true_value_roc, label='true ROC')
    #ax1.plot(time, measured_value_roc2, label='simple ratio ROC')
    #ax1.plot(time, measured_value_roc1, label='linear fit ROC')
    ax1.legend()
    ax1.set_xlim(0, NUM_POINTS)
    #ax1.set_ylim(-0.2, 1.2)
    plt.show()


# Generating the values and ROCs for the case when both the process formula and the ROC
# are unknown
def generate_temperature_profile3():
    time = np.linspace(0, NUM_POINTS - 1, NUM_POINTS)

    true_value = np.zeros(NUM_POINTS)

    for i in range(1, NUM_POINTS):
        true_value[i] = true_value[i - 1] + np.random.randn()

    #np.save('rw', true_value)
    #true_value = np.load('rw.npy')

    measured_value_roc1 = np.zeros(NUM_POINTS)
    measured_value_roc2 = np.zeros(NUM_POINTS)
    for i in range(MA_WINDOW, NUM_POINTS):
        measured_value_roc1[i] = np.polyfit(time[i - MA_WINDOW:i], true_value[i - MA_WINDOW:i], 1)[0]
        measured_value_roc2[i] = (true_value[i-MA_WINDOW] - true_value[i])/(time[i-MA_WINDOW]-time[i])

    f, ax1 = plt.subplots()
    #ax1.plot(time, true_value, label='true value')
    ax1.plot(time, measured_value_roc2, label='simple ratio ROC')
    ax1.plot(time, measured_value_roc1, label='linear fit ROC')
    ax1.legend()
    ax1.set_xlim(0, NUM_POINTS)
    plt.show()


generate_temperature_profile1()
