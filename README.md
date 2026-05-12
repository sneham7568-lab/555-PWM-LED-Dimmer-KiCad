
 """# 555 PWM LED Dimmer (KiCad PCB Design)

A PWM-based LED dimmer using the NE555 timer IC. The circuit controls LED brightness by adjusting the duty cycle with a potentiometer, while the entire workflow was designed in KiCad including schematic, PCB layout, 3D visualization, and fabrication-ready Gerber files.

---

## Features

- PWM generation using NE555 in astable mode
- Adjustable LED brightness using a 100k potentiometer
- Compact and beginner-friendly PCB layout
- Complete schematic + PCB + 3D design in KiCad
- PWM waveform visualization included
- Fabrication-ready Gerber outputs

---

## Components Used

| Component | Value / Part | Quantity |
|-----------|--------------|----------|
| Timer IC | NE555 | 1 |
| Resistor | 1kΩ | 1 |
| Resistor | 220Ω | 1 |
| Capacitor | 10µF | 1 |
| Capacitor | 0.01µF | 1 |
| Diode | 1N4148 | 2 |
| Potentiometer | 100k | 1 |
| LED | Standard 5mm or SMD | 1 |
| Power Supply | 12V DC | 1 |

---

## Working Principle

The NE555 timer operates in **astable PWM mode**.

A diode network (two 1N4148 diodes) creates separate charging and discharging paths for the timing capacitor. This allows the duty cycle of the output waveform to vary while maintaining an approximately constant frequency.

- **Low duty cycle** → Dim LED
- **High duty cycle** → Bright LED

The PWM signal is generated at **Pin 3** of the NE555 timer.

---

## PWM Output Waveform

By adjusting the potentiometer:

- ON time (TON) changes
- OFF time (TOFF) changes
- LED brightness changes accordingly

### Example Duty Cycles

| Duty Cycle | LED Brightness |
|------------|----------------|
| 25% | Dim |
| 50% | Medium |
| 75% | Bright |

The waveform images below demonstrate the PWM output at different duty cycles.

![PWM 25%](images/pwm_waveform_25.png)
![PWM 50%](images/pwm_waveform_50.png)
![PWM 75%](images/pwm_waveform_75.png)

---

## Preview Images

### Schematic Diagram
![Schematic](images/schematic.png)

### PCB Layout
![PCB Layout](images/pcb_layout.png)

### Routed PCB
![Routed PCB](images/routed_pcb.png)

### 3D PCB View
![3D View](images/3d_view.png)

---

## Project Structure

```plaintext
555-PWM-LED-Dimmer-KiCad/
├── schematic/
│   └── pwm_led_dimmer.kicad_sch
│
├── pcb/
│   └── pwm_led_dimmer.kicad_pcb
│
├── gerber/
│   ├── *.gbr
│   └── *.drl
│
├── images/
│   ├── schematic.png
│   ├── pcb_layout.png
│   ├── routed_pcb.png
│   ├── 3d_view.png
│   ├── pwm_waveform_25.png
│   ├── pwm_waveform_50.png
│   └── pwm_waveform_75.png
│
├── waveform/
│   └── pwm_waveform_generator.py
│
└── README.md
```

---

## PWM Waveform Generation

The PWM waveform images were generated using Python and Matplotlib.

Run the script inside the `waveform/` folder to regenerate the square-wave PWM signals:

```bash
cd waveform
python pwm_waveform_generator.py
```

---

## How to Use

1. Open the project in **KiCad**
2. Review the schematic and PCB layout
3. Generate Gerber files for fabrication (or use the pre-generated files in `gerber/`)
4. Assemble the PCB using the listed components
5. Power the circuit using a **12V supply**
6. Rotate the potentiometer to vary LED brightness

---

## Applications

- LED brightness control
- PWM signal generation
- Analog electronics learning
- Beginner PCB design project

---

## License

This project is open for educational and personal use. Feel free to modify and fabricate your own boards.
"""

with open("output/README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md generated successfully in output/README.md")
