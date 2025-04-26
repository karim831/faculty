import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import control as ctrl

# IMC-based PID Tuning Function
def imc_pid(K, tau, theta, lam):
    Kc = (tau + 0.5 * theta) / (K * (lam + 0.5 * theta))
    Ti = tau + 0.5 * theta
    Td = (tau * theta) / (2 * tau + theta)
    return Kc, Ti, Td

# Generate Closed-loop system
def get_closed_loop(tau, theta, lam):
    K = 1.0  # Set a default value for K
    Kc, Ti, Td = imc_pid(K, tau, theta, lam)

    # Plant G(s) = K / (tau*s + 1) * e^(-theta*s)
    plant = ctrl.tf([K], [tau, 1])
    delay = ctrl.pade(theta, 1)
    G = plant * ctrl.tf(*delay)

    # PID Controller C(s)
    C = Kc * (1 + ctrl.tf([1], [Ti]) + ctrl.tf([Td, 0], [1]))

    # Closed-loop system
    T = ctrl.feedback(C * G, 1)
    return T, (Kc, Ti, Td)

# Initial parameters
tau0, theta0, lam0, input0 = 1.0, 0.5, 1.0, 1.0

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.5)
t = np.linspace(0, 20, 1000)

system, (Kc0, Ti0, Td0) = get_closed_loop(tau0, theta0, lam0)
t_out, y_out = ctrl.step_response(system, t)
line, = ax.plot(t_out, y_out, label="System Output")
input_line, = ax.plot(t_out, input0 * np.ones_like(t_out), 'r--', label="Step Input")  # red dashed line for input
ax.set_title("Step Response with IMC Tuned PID")
ax.set_xlabel("Time")
ax.set_ylabel("Output")
ax.legend()
ax.set_ylim(-2, 2)

# Sliders for parameters
axcolor = 'lightgoldenrodyellow'
slider_axes = {
    'tau': plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor),
    'theta': plt.axes([0.25, 0.30, 0.65, 0.03], facecolor=axcolor),
    'lambda': plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor),
    'input': plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
}
sliders = {
    'tau': Slider(slider_axes['tau'], 'Tau', 0.1, 10.0, valinit=tau0),
    'theta': Slider(slider_axes['theta'], 'Theta', 0.0, 5.0, valinit=theta0),
    'lambda': Slider(slider_axes['lambda'], 'Lambda', 0.1, 10.0, valinit=lam0),
    'input': Slider(slider_axes['input'], 'Input', 0.1, 5.0, valinit=input0)
}

def update(val):
    tau = sliders['tau'].val
    theta = sliders['theta'].val
    lam = sliders['lambda'].val
    input_amp = sliders['input'].val

    new_sys, (Kc, Ti, Td) = get_closed_loop(tau, theta, lam)
    t_out, y_out = ctrl.step_response(new_sys, t)
    line.set_ydata(y_out * input_amp)  # scale output according to input
    input_line.set_ydata(input_amp * np.ones_like(t_out))  # adjust input line

    # Update text labels for Kp, Ki, Kd
    kp_text.set_text(f"Kp: {Kc:.2f}")
    ki_text.set_text(f"Ki: {Kc/Ti:.2f}")  # Corrected Ki formula
    kd_text.set_text(f"Kd: {Kc*Td:.2f}")  # Corrected Kd formula
    
    fig.canvas.draw_idle()

for slider in sliders.values():
    slider.on_changed(update)

# Enable zoom and pan interactivity in the plot
plt.rcParams['toolbar'] = 'toolbar2'  # Add this line to enable zoom toolbar

plt.show()
