<h1 align="center">
<img src="https://github.com/acentauri-solar-racing/ss_performance_toolbox/blob/dev/logo/logo.png?raw=true" width="300">
</h1>

# Strategy and Simulation Interview Question

Welcome to the aCentauri Solar Racing Team! Thank you for your interest in the strategy and simulation subsystem.

To better assess your skills, we have prepared the following task, which you have 20 minutes to complete. Afterwards, we will discuss your approach and implementation. Try your best! There are many possibilities for solving this task.

## Task Description

You are part of aCentauri as a strategy and simulation engineer. The other subsystems have designed several car options which we now want to compare to find the best car design for the BWSC 2025.

**The best car is the one that finishes the race the fastest.**

Implement your solution in the provided `main.py` file.

### Data

The parameters of the different cars are stored in the `car.csv` file. The following parameters are given:

| Parameter | CSV | Description | Unit |
|-----------|-----|-------------|------|
| $m$ | `m` | Total mass of the car including driver | $\mathrm{kg}$ |
| $A_\mathrm{front}$ | `A_front` | Frontal area of the car | $\mathrm{m^2}$ |
| $A_\mathrm{pv}$ | `A_pv` | Area of the PV cells | $\mathrm{m^2}$ |
| $f_\mathrm{s}$ | `f_s` | Fraction of the PV cells that are shaded on average | - |
| $c_\mathrm{d}$ | `c_d` | Aerodynamic friction coefficient | - |
| $c_\mathrm{r}$ | `c_r` | Rolling friction coefficient | - |
| $E_\mathrm{bat}$ | `E_bat` | Capacity of the battery | $\mathrm{kWh}$ |
| $P_\mathrm{motor}$ | `P_motor` | Maximum motor power output | $\mathrm{kW}$ |
| $\eta_\mathrm{pv}$ | `eta_pv` | Efficiency of the PV panels | - |
| $\eta_\mathrm{motor}$ | `eta_motor` | Efficiency of the motor | - |
| $\eta_\mathrm{bat}$ | `eta_bat` | Charging and discharging efficiency of the battery | - |

Feel free to use the parameters that you think are the most important ones. There is definitely no need to include all of them in this analysis.

In addition, we know the following about the BWSC 2025 route (stored in `route.csv`):

| Parameter | CSV | Description | Unit |
|-----------|-----|-------------|------|
| $i$ | `index` | Index of the point | - |
| $s_i$ | `distance` | Distance from the start | $\mathrm{km}$ |
| $h_i$ | `elevation` | Elevation of the road | $\mathrm{m}$ |

Finally, an average solar irradiance of $I_\mathrm{sun} = 700\ \mathrm{W}$ and an air density of $\rho_\mathrm{air} = 1.17\ \mathrm{kg/m^3}$ can be assumed for the entire route. The cars are expected to roughly drive at $v = 90\ \mathrm{km/h}$.

## Expected Results
- Design a metric that allows you to compare the cars as accurately as possible for the given route data.
- Implement this metric in Python and provide a ranking for the given cars.

## Hints
- Examine the route data, as this defines the main objective the car has to fulfill.
- Due to time restrictions, focus on the most important parameters.
- As a quick reminder:
  - Aerodynamic drag force: $F_\mathrm{aero} = \frac{1}{2} \cdot \rho_\mathrm{air} \cdot A_\mathrm{front} \cdot c_\mathrm{d} \cdot v^2$
  - Rolling resistance force: $F_\mathrm{roll} = m \cdot g \cdot \cos(\alpha) \cdot c_\mathrm{r}$

**We are very happy to see your solution to this problem! :)**
