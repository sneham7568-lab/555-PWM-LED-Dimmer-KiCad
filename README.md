
 555 PWM LED Dimmer (KiCad PCB Design)

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


---

## Project Structure

```plaintext
555-PWM-LED-Dimmer-KiCad/
│
├── schematic/
│   ├── PWM_LED_DIMMER.kicad_sch
│   ├── pwm_led_dimmer.pdf
│   └── schematic.png
│
├── pcb/
│   ├── PWM_LED_DIMMER.kicad_pcb
│   ├── PWM_LED_DIMMER.kicad_pro
│   └── routed_pcb.png
│
├── gerber/
│   ├── PWM_LED_DIMMER-F_Cu.gbr
│   ├── PWM_LED_DIMMER-B_Cu.gbr
│   ├── PWM_LED_DIMMER-F_Silkscreen.gbr
│   ├── PWM_LED_DIMMER-Edge_Cuts.gbr
│   ├── PWM_LED_DIMMER-job.gbrjob
│   ├── PWM_LED_DIMMER-PTH.drl
│   └── PWM_LED_DIMMER-NPTH.drl
│
├── images/
│   ├── 3d_view.png
│   ├── pcb_layout.png
│   ├── silkscreen_layer.png
│   └── fabrication_layer.png
│
├── waveform/
│   ├── pwm_waveform.png
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


