## Classifying a differential equation {#classification}

**Ordinary** means one independent variable. The **order** is the highest derivative that appears. For **linear**, look at the dependent variable and its derivatives. Each occurs to the first power with a coefficient depending only on the independent variable.

For example, $\sin(x)y'+\ln(x)y=\tan(e^x)$ is first-order and linear on $x>0$ wherever the right side is defined. In $y''+xy'+\sin y=0$, the term $\sin y$ makes a second-order equation nonlinear.

An **initial value problem** (IVP) specifies the equation and initial data. Find the general solution first, keeping the integration constants. Use the initial data to select a particular solution on an interval containing the initial point.

## Direction fields and integral curves {#direction-fields}

For $y'=f(t,y)$, evaluate $f$ at a grid of points $(t,y)$. At each point draw a short segment of that slope. To sketch an **integral curve**, start at the initial point and follow those segments. A scalar solution $y(t)$ has one value at each $t$ in its interval.

### Example · Reading the slopes of $y'=y$

Along $y=0$ the segments are horizontal. Above this line the slopes are positive, below it they are negative, and their magnitude increases with $|y|$. Separating variables gives $\ln|y|=t+C$ for $y\ne0$. The family $y=Ce^t$ includes the horizontal solution when $C=0$.

{{figure:growth}}

For the field $\frac{dy}{dx}=-\frac{2x}{y}$, the slope is zero on $x=0$ wherever $y\ne0$, and the equation is undefined on $y=0$. Sketch solution branches only where the slope is defined.

{{figure:ellipse}}

## Calculus reminders {#calculus}

| Function | Derivative | Antiderivative, up to a constant |
|:---|:---|:---|
| $x^n$ | $nx^{n-1}$ | $\frac{x^{n+1}}{n+1}$ for $n\ne-1$ |
| $e^x$ | $e^x$ | $e^x$ |
| $\sin x$ | $\cos x$ | $-\cos x$ |
| $\cos x$ | $-\sin x$ | $\sin x$ |

The exceptional exponent $n=-1$ gives $\int\frac{1}{x}\,dx=\ln|x|+C$. Also remember $(\tan x)'=\sec^2 x$, so $\int\sec^2 x\,dx=\tan x+C$.

**Integration by parts.** Choose $u$ so differentiating simplifies it, and choose $dv$ you can integrate. Then $\int u\,dv=uv-\int v\,du$. For $\int xe^x\,dx$, take $u=x$ and $dv=e^x\,dx$. This gives $xe^x-\int e^x\,dx=xe^x-e^x+C$.

**Partial derivatives.** Hold the other variable fixed.

$$f_x(x,y)=\lim_{h\to0}\frac{f(x+h,y)-f(x,y)}{h},\qquad
f_y(x,y)=\lim_{h\to0}\frac{f(x,y+h)-f(x,y)}{h}.$$

For $f(x,y)=x^2y+e^y$, this gives $f_x=2xy$ and $f_y=x^2+e^y$.

**Double angles.**

$$\begin{aligned}
\sin(2\theta)&=2\sin\theta\cos\theta,\\
\cos(2\theta)&=\cos^2\theta-\sin^2\theta\\
&=2\cos^2\theta-1.
\end{aligned}$$
