Our system is defined by the equation:

$$\ddot{x}=-\frac{5g}{7}\theta$$

The input to the system is $$\theta$$ and the output from the system is considered as the distance of the ball from the centre of the plate axis of rotation.

The position is obtained by using odeint function in SciPy library with initial position and velocity of the ball considerd as [0, 0].

The Simulation is done for 1000 time steps

The setpoint is calculated when the user clicks on the simulation window and the point where the User clicks is captured and the setpoint is the distance between the plate axis of rotation and the clicked point. 

Note: Only X coordinates of the mouse click is considered for setpoint calculation.

The error is considered as the difference between the current position (x coordinate) and the set point.

This error is fed to the P controller which calculates the input to the system ($$\theta$$)

The Tuning of K_p is done manually for desired performance.

P controller is implemented for the 
