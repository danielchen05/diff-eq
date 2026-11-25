## Foundations {#basics}

### Classifying an equation {#classification}

An ordinary differential equation has one independent variable. Its highest derivative gives the **order**. In a **linear** ODE, $y$ and its derivatives occur only to the first power, each with a coefficient depending only on the independent variable.

### Direction fields {#direction-fields}

For $y'=f(t,y)$, draw a segment of slope $f(t,y)$ at $(t,y)$. An integral curve through $(t_0,y_0)$ follows those segments.

### Calculus reminders {#calculus}

| Function | Derivative | Antiderivative, up to a constant |
|:---|:---|:---|
| $x^n$ | $nx^{n-1}$ | $\frac{x^{n+1}}{n+1}$ for $n\ne-1$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ | $\ln\lvert x\rvert$ |
| $e^x$ | $e^x$ | $e^x$ |
| $\sin x$ | $\cos x$ | $-\cos x$ |
| $\cos x$ | $-\sin x$ | $\sin x$ |

**Integration by parts.** $\displaystyle\int u\,dv=uv-\int v\,du$. Also, $(\tan x)'=\sec^2 x$.

**Partial derivatives.** Hold the other variable fixed.

$$f_x=\lim_{h\to0}\frac{f(x+h,y)-f(x,y)}{h},$$
$$f_y=\lim_{h\to0}\frac{f(x,y+h)-f(x,y)}{h}.$$

**Double angles.** $\sin(2\theta)=2\sin\theta\cos\theta$ and $\cos(2\theta)=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1$.

## First-order ODEs {#first-order}

### Separation of variables {#separation}

For $y'=g(t)h(y)$, save the constant solutions from $h(y)=0$. Where $h(y)\ne0$, separate and integrate.

$$\int\frac{dy}{h(y)}=\int g(t)\,dt+C.$$

### Integrating factors {#integrating-factor}

Normalize to $y'+p(t)y=q(t)$ where the leading coefficient is nonzero. Multiply the whole equation by $\mu$.

$$\mu(t)=e^{\int p(t)\,dt},$$ $$(\mu y)'=\mu q,$$
$$y=\frac{1}{\mu}\left(\int\mu q\,dt+C\right).$$

### Exact equations {#exact}

For $M\,dx+N\,dy=0$, test $M_y=N_x$ on a rectangle with continuous first partials. From $\phi_x=M$, integrate $\phi=\int M\,dx+h(y)$. Match $\phi_y=N$ to find $h$, then write $\phi(x,y)=C$.

## Existence and phase lines {#qualitative}

### Existence and uniqueness {#existence}

**Linear IVP.** For $y'+py=q$, continuous $p,q$ on an open interval containing $t_0$ give a unique solution throughout it. Normalize first.

**Nonlinear IVP.** For $y'=f(t,y)$ with $y(t_0)=y_0$, check an **open rectangle around the initial point** $(t_0,y_0)$.

| What to check throughout the rectangle | What it guarantees near $t_0$ |
|:---|:---|
| $f$ is continuous | At least one local solution exists. |
| In addition, $f_y=\partial f/\partial y$ exists and is continuous | The local solution is unique. |

### Autonomous equations {#phase-lines}

For $y'=f(y)$, solve $f(y)=0$. Between roots, draw an arrow to the right for $f(y)>0$ and to the left for $f(y)<0$. Read the two arrows next to each equilibrium.

| Arrows at the equilibrium | Classification |
|:---|:---|
| $\rightarrow\,\bullet\,\leftarrow$ Both point in | Stable |
| $\leftarrow\,\bullet\,\rightarrow$ Both point out | Unstable |
| $\rightarrow\,\bullet\,\rightarrow$ or $\leftarrow\,\bullet\,\leftarrow$ Both point the same way | Semi-stable |

### Bifurcations {#bifurcations}

For $x'=f(x;c)$, plot the equilibria $f(x;c)=0$ against $c$. A **bifurcation value** is a value of $c$ where the number or stability of equilibria changes. In these diagrams, read the $c$-coordinate wherever two equilibrium branches meet. Check the phase lines just before, at, and just after that value.

## Second-order homogeneous ODEs {#homogeneous}

### Characteristic roots {#real-roots}

For $ay''+by'+cy=0$ with constants and $a\ne0$, substitute $y=e^{rt}$ and solve $ar^2+br+c=0$.

| Roots | General real solution |
|:---|:---|
| Distinct real $r_1,r_2$ | $C_1e^{r_1t}+C_2e^{r_2t}$ |
| Repeated real $r$ | $(C_1+C_2t)e^{rt}$ |
| $\lambda\pm i\mu$, $\mu\ne0$ | $e^{\lambda t}(C_1\cos(\mu t)+C_2\sin(\mu t))$ |

**Euler's formula.** $e^{i\theta}=\cos\theta+i\sin\theta$.

### Superposition and the Wronskian {#wronskian}

Let $y_1,y_2$ solve the same second-order linear homogeneous ODE with continuous normalized coefficients on an interval $I$. Their Wronskian is

$$W(t)=y_1y_2'-y_1'y_2.$$

- If $W(t_0)\ne0$ at **one point** $t_0\in I$, the solutions are linearly independent and form a **fundamental set** on $I$.
- If $W(t)=0$ at **every point** of $I$, the solutions are linearly dependent.

For a fundamental set, the general solution is $y=C_1y_1+C_2y_2$. To find the constants, evaluate every function in the system below at $t_0$.

$$\begin{pmatrix}y_1&y_2\\y_1'&y_2'\end{pmatrix}
\binom{C_1}{C_2}=\binom{y}{y'}.$$

### Abel's formula {#abel}

For $y''+p(t)y'+q(t)y=0$ with $p,q$ continuous on the interval,

$$W(t)=W(t_0)e^{-\int_{t_0}^{t}p(s)\,ds}.$$

### Reduction of order {#repeated-roots}

Given a solution $y_1$ of $y''+py'+qy=0$, work on an interval where $y_1\ne0$. Set $y_2=vy_1$. With $w=v'$, solve $y_1w'+(2y_1'+py_1)w=0$, choose a nonzero solution for $w$, and integrate $v'=w$.

## Second-order nonhomogeneous ODEs {#nonhomogeneous}

### Homogeneous plus particular {#particular}

For $L[y]=g$, solve $L[y_h]=0$ and find one $Y$ with $L[Y]=g$. Apply initial conditions to the full solution $y=y_h+Y$.

### Undetermined coefficients {#undetermined}

Use this method for a linear ODE with constant coefficients.

| Forcing | Initial trial |
|:---|:---|
| Polynomial of degree $n$ | $A_nt^n+\cdots+A_1t+A_0$ |
| $e^{at}$ | $Ae^{at}$ |
| $\sin(bt)$ or $\cos(bt)$ | $A\cos(bt)+B\sin(bt)$ |

**Resonance.** Multiply the whole trial by $t^s$ if the corresponding characteristic root has multiplicity $s$. For a polynomial times a sine or cosine, use a full polynomial for each trigonometric term.

### Variation of parameters {#variation}

Normalize to $y''+py'+qy=g$. Choose a **fundamental set** $\{y_1,y_2\}$ for the homogeneous equation, with Wronskian $W\ne0$. Write $Y=u_1y_1+u_2y_2$.

$$u_1'=-\frac{y_2g}{W},$$ $$u_2'=\frac{y_1g}{W}.$$

$$Y=-y_1\int\frac{y_2g}{W}\,dt+y_2\int\frac{y_1g}{W}\,dt.$$

## Higher-order ODEs {#higher-order-odes}

### Characteristic equations and multiplicity {#higher-order}

For a homogeneous equation with real constant coefficients and $a_n\ne0$, substitute $y=e^{rt}$ and solve

$$P(r)=\sum_{j=0}^n a_jr^j=0.$$

| Root of multiplicity $m$ | Solutions for $k=0,\ldots,m-1$ |
|:---|:---|
| Real root $r$ | $t^k e^{rt}$ |
| Pair $\alpha\pm i\beta$, $\beta\ne0$ | $t^k e^{\alpha t}\cos(\beta t)$ and $t^k e^{\alpha t}\sin(\beta t)$ |

Combine all $n$ independent solutions. The initial values $y(t_0),\ldots,y^{(n-1)}(t_0)$ determine a unique solution on an interval of continuous normalized coefficients and forcing containing $t_0$.

### Higher-order undetermined coefficients {#higher-order-forcing}

Use the [same rule as for second-order ODEs](#formula-undetermined). Choose a trial for each forcing term. If any term in a trial repeats a homogeneous solution, multiply the **whole trial** by $t$. Repeat until there is no overlap. Substitute to find the coefficients, then write $y=y_h+Y$.

## Linear systems {#systems}

### Converting an equation to a system {#conversion}

Set $x_1=y,\ x_2=y',\ldots,x_n=y^{(n-1)}$. Then $x_1'=x_2,\ldots,x_{n-1}'=x_n$. Use the original equation for $x_n'$. Continuous $A(t),\mathbf g(t)$ in $\mathbf x'=A(t)\mathbf x+\mathbf g(t)$ give a unique solution for each initial vector on that interval.

### Eigenvalues and eigenvectors {#matrices}

Solve $\det(A-rI)=0$, then $(A-rI)\mathbf v=\mathbf0$ for $\mathbf v\ne\mathbf0$. Check $A\mathbf v=r\mathbf v$. For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, solve $r^2-(a+d)r+(ad-bc)=0$.

### Independent real eigenvectors {#real-systems}

For $\mathbf x'=A\mathbf x$ with constant $A$, each eigenpair gives a solution $e^{r_jt}\mathbf v_j$. In dimension $n$, combine $n$ independent solutions. For a real $2\times2$ matrix with two independent real eigenvectors, the general solution is $\mathbf x=C_1e^{r_1t}\mathbf v_1+C_2e^{r_2t}\mathbf v_2$.

### Complex eigenvalues {#complex-systems}

For a real constant $2\times2$ matrix $A$ with a complex eigenvalue $r=\lambda+i\mu$, write its eigenvector as $\mathbf v=\mathbf a+i\mathbf b$ and let $\theta=\mu t$. The general real solution of $\mathbf x'=A\mathbf x$ is $\mathbf x=C_1\mathbf x_1+C_2\mathbf x_2$.

$$\begin{aligned}
\mathbf x_1&=e^{\lambda t}(\mathbf a\cos\theta-\mathbf b\sin\theta),\\
\mathbf x_2&=e^{\lambda t}(\mathbf a\sin\theta+\mathbf b\cos\theta).
\end{aligned}$$

In a $3\times3$ system with a real eigenvalue and a complex conjugate pair, include the solution for the real eigenvalue as well.

### Repeated eigenvalues {#repeated-systems}

For a real constant $2\times2$ matrix $A$ with a double eigenvalue $r$ and one independent eigenvector $\mathbf v$, solve $(A-rI)\mathbf w=\mathbf v$. The general solution of $\mathbf x'=A\mathbf x$ is

$$\mathbf x=e^{rt}[C_1\mathbf v+C_2(t\mathbf v+\mathbf w)].$$

### Fundamental matrices and the system Wronskian {#fundamental-matrix}

For the homogeneous system $\mathbf x'=A(t)\mathbf x$, place $n$ solution vectors **side by side as columns** of $\Phi$. Their Wronskian is its determinant. If $W(t_0)\ne0$ and $A(t)$ is continuous on an interval containing $t_0$, $\Phi$ is a fundamental matrix there.

$$\Phi=\begin{bmatrix}\mathbf x^{(1)}&\cdots&\mathbf x^{(n)}\end{bmatrix},$$
$$W(t)=\det\Phi(t).$$

**Initial data.** In $\mathbf x(t)=\Phi(t)\mathbf c$, solve $\Phi(t_0)\mathbf c=\mathbf x(t_0)$. Equivalently, $\mathbf x(t)=\Phi(t)\Phi(t_0)^{-1}\mathbf x(t_0)$. **Recover the system.** $A=\Phi'\Phi^{-1}$.

### Linear phase portraits {#phase-portraits}

Find the eigenvalues of $A$ in $\mathbf x'=A\mathbf x$. Order real eigenvalues as $r_1\le r_2$. In the complex rows, $\mu>0$.

| Eigenvalues | Linear type | Stability |
|:---|:---|:---|
| $r_1<0<r_2$ | Saddle | Unstable |
| $r_1<r_2<0$ | Node (sink) | Asymptotically stable |
| $0<r_1<r_2$ | Node (source) | Unstable |
| $r_1=r_2<0$, one independent eigenvector | Improper node | Asymptotically stable |
| $r_1=r_2>0$, one independent eigenvector | Improper node | Unstable |
| $\lambda\pm i\mu$, $\lambda<0$ | Spiral node (spiral sink) | Asymptotically stable |
| $\lambda\pm i\mu$, $\lambda>0$ | Spiral node (spiral source) | Unstable |
| $\pm i\mu$ | Center | Stable |

Trajectories approach a sink and move away from a source. Around a center, nearby trajectories stay on closed curves. Evaluate $A\mathbf x$ at a convenient point to orient the arrows.

## Nonlinear systems {#nonlinear}

### Equilibria and the Jacobian {#linearization}

Solve $F(x,y)=G(x,y)=0$. At each equilibrium $\mathbf p$, set $\mathbf u=\mathbf x-\mathbf p$. The linearization is $\mathbf u'=J(\mathbf p)\mathbf u$, where $J=\begin{pmatrix}F_x&F_y\\G_x&G_y\end{pmatrix}$.

### What linearization preserves {#preservation}

Use the eigenvalues of the Jacobian at the equilibrium. For a system with continuous first partial derivatives, distinct eigenvalues with nonzero real parts preserve both local type and stability. In the complex rows, $\mu>0$.

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

A repeated nonzero eigenvalue with two independent eigenvectors gives the same stability conclusions as the repeated-root rows.

### Polar coordinates and limit cycles {#cycles}

**Convert to polar.** Differentiate $r^2=x^2+y^2$ and, where $x\ne0$, $\theta=\tan^{-1}(y/x)$ with the angle adjusted by $\pi$ for $x<0$. Substitute $x=r\cos\theta$ and $y=r\sin\theta$. The formulas hold for $r>0$.

$$r'=\frac{xx'+yy'}{r},$$ $$\theta'=\frac{xy'-yx'}{r^2}.$$

1. **Find the circles.** For $r'=f(r)$, solve $f(r)=0$ and keep $r>0$. An isolated positive root gives a circular **limit cycle** if $\theta'\ne0$ everywhere on the circle. Check $r=0$, the origin, separately.
2. **Classify stability.** Draw a phase line for $r$, just as for a [first-order autonomous ODE](#formula-phase-lines). On either side of each root, $r'>0$ points toward larger radii and $r'<0$ toward smaller radii. Both arrows in mean stable, both out mean unstable, and both pointing the same way mean semi-stable.
3. **Read the rotation.** $\theta'>0$ means counterclockwise. $\theta'<0$ means clockwise.

A closed trajectory encloses at least one equilibrium if the system is smooth everywhere on and inside that trajectory.

## Laplace transforms {#laplace}

### Definition {#laplace-definition}

$\displaystyle F(s)=\mathcal L\{f\}(s)=\int_0^\infty e^{-st}f(t)\,dt$ where the integral converges.

### Initial value problems {#laplace-ivp}

With $Y(s)=\mathcal L\{y\}(s)$, transform both sides, insert the initial data, solve for $Y$, and invert. Use partial fractions when needed.

$$\mathcal L\{y'\}=sY-y(0),$$ $$\mathcal L\{y''\}=s^2Y-sy(0)-y'(0).$$

### Step functions {#steps}

For $c\ge0$ and $s>0$,

$$u_c(t)=\begin{cases}0,&t<c,\\1,&t\ge c,\end{cases}$$
$$\mathcal L\{u_c\}(s)=\frac{e^{-cs}}{s}.$$

## Euler’s method {#numerical}

### Forward Euler {#euler}

For $y'=f(t,y)$, one tangent step from exact data gives $y(t_0+h)\approx y_0+h f(t_0,y_0)$. For successive steps, evaluate the slope at the **current numerical point**.

$$t_{n+1}=t_n+h,$$ $$y_{n+1}=y_n+h f(t_n,y_n).$$
