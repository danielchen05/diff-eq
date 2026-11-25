## Characteristic equations and multiplicity {#higher-order}

For a linear ODE with **constant coefficients**, find the homogeneous solution first. In $a_ny^{(n)}+\cdots+a_1y'+a_0y=0$, substitute $y=e^{rt}$ and cancel the exponential to get the characteristic equation.

$$P(r)=a_nr^n+\cdots+a_1r+a_0=0.$$

The leading coefficient satisfies $a_n\ne0$, so $P$ has degree $n$.

1. Factor $P$. A real root $r$ of multiplicity $m$ gives $e^{rt},te^{rt},\ldots,t^{m-1}e^{rt}$.
2. A complex pair $\alpha\pm i\beta$ gives $e^{\alpha t}\cos(\beta t)$ and $e^{\alpha t}\sin(\beta t)$. For a repeated pair, multiply both by $t^k$ for $k=0,\ldots,m-1$, where $m$ is the multiplicity of each root.
3. Combine all $n$ independent solutions. An order-$n$ IVP specifies $y(t_0),y'(t_0),\ldots,y^{(n-1)}(t_0)$. Continuous normalized coefficients and forcing on an interval containing $t_0$ give a unique solution there.

## Higher-order undetermined coefficients {#higher-order-forcing}

Use the [same rule as for second-order ODEs](#undetermined).

1. Find $y_h$. Choose a trial with undetermined coefficients for each forcing term.
2. Compare that trial with $y_h$. If any term repeats a homogeneous solution, multiply the **whole trial** by $t$. Keep multiplying by $t$ until there is no overlap.
3. Substitute the trials into the ODE and match coefficients to find $Y$. Apply the initial conditions to $y=y_h+Y$.

**Recognizing resonance.** For $y'''-3y''+3y'-y=e^t$, the characteristic polynomial is $(r-1)^3$. The functions $e^t$, $te^t$, and $t^2e^t$ are all homogeneous solutions, so the first independent trial is $Y=At^3e^t$.
