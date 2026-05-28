import numpy as np
import matplotlib.pyplot as plt

# PWM waveform generator function
def generate_pwm_waveform(duty_cycle, filename):

    frequency = 1000      # 1 kHz
    amplitude = 5         # 5V PWM signal

    # Time axis
    t = np.linspace(0, 2e-3, 2000)

    # PWM signal generation
    pwm = amplitude * (
        (t % (1 / frequency))
        < (duty_cycle / 100) * (1 / frequency)
    )

    # Plot
    plt.figure(figsize=(10, 4))
    plt.plot(
        t * 1000,
        pwm,
        linewidth=2,
        label=f"{duty_cycle}% Duty Cycle"
    )

    plt.title(
        f"PWM Waveform using NE555 Timer ({duty_cycle}% Duty Cycle)"
    )

    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (V)")

    plt.ylim(-0.5, 5.5)

    plt.grid(True)
    plt.legend()

    # Save image
    plt.savefig(
        filename,
        dpi=300,
        bbox_inches='tight'
    )

    plt.close()


# Generate multiple duty cycle waveforms

generate_pwm_waveform(25, "pwm_waveform_25.png")
generate_pwm_waveform(50, "pwm_waveform_50.png")
generate_pwm_waveform(75, "pwm_waveform_75.png")

print("PWM waveform images generated successfully!")