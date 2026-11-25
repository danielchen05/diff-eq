## Equilibria and the Jacobian {#linearization}

For an autonomous system in two variables, $x'=F(x,y)$, $y'=G(x,y)$, an **equilibrium** or **critical point** solves **both** $F=0$ and $G=0$. Keep only ordered pairs satisfying both equations.

1. Compute the Jacobian before substituting any point.
2. At each equilibrium $\mathbf p$, evaluate $J(\mathbf p)$. In displacement coordinates $\mathbf u=\mathbf x-\mathbf p$ the linearized system is $\mathbf u'=J(\mathbf p)\mathbf u$.
3. Find its eigenvalues, classify the linear system, and decide which conclusions transfer to the original equilibrium.

$$J(x,y)=\begin{pmatrix}F_x&F_y\\G_x&G_y\end{pmatrix}.$$

For instance, in $x'=y-x^2,\ y'=1-y$, the second equilibrium equation gives $y=1$. The first then gives $x=\pm1$. Evaluate the Jacobian **separately** at these two points.

A phase-plane trajectory is the path traced by $(x(t),y(t))$. For the system $x'=4-2y$, $y'=12-3x^2$, the velocity at each point is $(4-2y,12-3x^2)$. Its two components give the horizontal and vertical directions of motion.

## What linearization preserves {#preservation}

Evaluate the Jacobian at the equilibrium. Assume the system has continuous first partial derivatives nearby. If its two eigenvalues are distinct and both have nonzero real part, both the type and stability of the [linear phase portrait](#phase-portraits) carry over locally. In the complex rows, $\mu>0$.

::: {.stability-comparison}
| Eigenvalues | Linear type | Linear stability | Nonlinear type | Nonlinear stability |
|:---|:---|:---|:---|:---|
| $r_1<0<r_2$ | Saddle | Unstable | Saddle | Unstable |
| $r_1<r_2<0$ | Node (sink) | Asymptotically stable | Node (sink) | Asymptotically stable |
| $0<r_1<r_2$ | Node (source) | Unstable | Node (source) | Unstable |
| $\lambda\pm i\mu$, $\lambda<0$ | Spiral sink | Asymptotically stable | Spiral sink | Asymptotically stable |
| $\lambda\pm i\mu$, $\lambda>0$ | Spiral source | Unstable | Spiral source | Unstable |
| $r_1=r_2<0$, one independent eigenvector | Improper node | Asymptotically stable | Inconclusive | Asymptotically stable |
| $r_1=r_2>0$, one independent eigenvector | Improper node | Unstable | Inconclusive | Unstable |
| $\pm i\mu$ | Center | Stable | Inconclusive | Inconclusive |
:::

A repeated nonzero eigenvalue with two independent eigenvectors gives the same stability conclusions as the repeated-root rows. For a complex pair, check the real parts. A purely imaginary pair can satisfy $\det J\ne0$.

## Polar coordinates and limit cycles {#cycles}

Use $x=r\cos\theta$ and $y=r\sin\theta$. Two identities give the radial and angular equations.

1. Differentiate $r^2=x^2+y^2$. This gives $2rr'=2xx'+2yy'$. Divide by $2r$ for $r>0$.
2. Where $x\ne0$, use $\theta=\tan^{-1}(y/x)$, adding $\pi$ for $x<0$ to select the correct quadrant. The constant drops out when differentiating. This gives $\theta'=\frac{1}{1+(y/x)^2}\frac{xy'-yx'}{x^2}$. Simplify the denominator using $x^2+y^2=r^2$.

The resulting formulas hold everywhere $r>0$. Substitute the original $x'$ and $y'$ and simplify in terms of $r$ and $\theta$.

$$r'=\frac{xx'+yy'}{r},$$ $$\theta'=\frac{xy'-yx'}{r^2}.$$

### Finding and classifying a circular limit cycle

A **limit cycle** is a closed trajectory isolated from other closed trajectories.

1. **Find the radius.** For $r'=f(r)$, solve $f(r)=0$ for $r>0$. A root gives a circle of constant radius. It is a limit cycle when the radius is isolated and $\theta'\ne0$ all the way around the circle. Check $r=0$, the origin, in the original system.
2. **Draw a radial phase line.** Test the sign of $r'$ between roots, just as for a [first-order autonomous ODE](#phase-lines). Draw an arrow toward larger $r$ when $r'>0$ and toward smaller $r$ when $r'<0$. At each cycle, both arrows in mean stable, both out mean unstable, and both pointing the same way mean semi-stable.
3. **Give the rotation.** $\theta'>0$ means counterclockwise and $\theta'<0$ means clockwise.

A closed trajectory encloses at least one equilibrium if the system is smooth everywhere on and inside that trajectory.

### Example · One stable cycle

For $r'=r(1-r)$, $\theta'=1$, the radial velocity is positive on $(0,1)$ and negative for $r>1$. Both phase-line arrows point toward $r=1$, so this circle is a stable limit cycle. Motion is counterclockwise.

### Example · Two cycles rotating clockwise

For $r'=r(1-r)(r-2)$, $\theta'=-1$, the radial signs on $(0,1)$, $(1,2)$, and $(2,\infty)$ are $-,+,-$. Small positive radii decrease toward the stable origin. Both arrows point away from $r=1$, giving an unstable cycle, and toward $r=2$, giving a stable cycle. Both rotate clockwise.

{{figure:radial}}
