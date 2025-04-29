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
    K = 1.0  # Process gain
    Kc, Ti, Td = imc_pid(K, tau, theta, lam)

    # Plant G(s) = K / (tau*s + 1) * e^(-theta*s)
    plant = ctrl.tf([K], [tau, 1])
    delay = ctrl.pade(theta, 1)
    G = plant * ctrl.tf(*delay)

    # PID Controller with corrected integral term
    C_pid = Kc * (ctrl.tf([1], [1, 0]) + ctrl.tf([1], [Ti, 0]) + ctrl.tf([Td, 0], [1]))
    
    # Closed-loop system
    T = ctrl.feedback(C_pid * G, 1)
    return T, (Kc, Ti, Td)

# Initial parameters
tau0, theta0, lam0 = 1.0, 0.5, 1.0
input_amp = 1  # Fixed input at 1

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)
t = np.linspace(0, 1000, 5000)

system, (Kc0, Ti0, Td0) = get_closed_loop(tau0, theta0, lam0)
t_out, y_out = ctrl.step_response(system, t)
line, = ax.plot(t_out, y_out * input_amp, label="Step Response")
input_line, = ax.plot(t_out, input_amp * np.ones_like(t_out), 'r--', label="Step Input")
ax.set_title("Step Response with Lambda Tuned PID")
ax.set_xlabel("Time")
ax.set_ylabel("Step Input and Response")
ax.legend()
ax.set_ylim(-0.5, 2.0)  # Adjusted ylim for better visualization

# Sliders for parameters
axcolor = 'lightgoldenrodyellow'
slider_axes = {
    'tau': plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor),
    'theta': plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor),
    'lambda': plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
}
sliders = {
    'tau': Slider(slider_axes['tau'], 'Tau', 0.1, 10.0, valinit=tau0),
    'theta': Slider(slider_axes['theta'], 'Theta', 0.0, 5.0, valinit=theta0),
    'lambda': Slider(slider_axes['lambda'], 'Lambda', 0.1, 100.0, valinit=lam0)
}

def update(val):
    tau = sliders['tau'].val
    theta = sliders['theta'].val
    lam = sliders['lambda'].val

    new_sys, (Kc, Ti, Td) = get_closed_loop(tau, theta, lam)
    t_out, y_out = ctrl.step_response(new_sys, t)
    line.set_ydata(y_out * input_amp)
    input_line.set_ydata(input_amp * np.ones_like(t_out))    
    fig.canvas.draw_idle()

for slider in sliders.values():
    slider.on_changed(update)

plt.show()