## From one equation to a system {#conversion}

For an order-$n$ equation solved for its highest derivative, set $x_1=y,\ x_2=y',\ldots,x_n=y^{(n-1)}$. Then $x_1'=x_2,\ldots,x_{n-1}'=x_n$, and the original equation supplies $x_n'$.

### Example · Converting a forced second-order equation

For $y''+2y'+y=t$, take $x_1=y$ and $x_2=y'$. Then $x_1'=x_2$ and $x_2'=-x_1-2x_2+t$, or

$$\mathbf x'=\begin{pmatrix}0&1\\-1&-2\end{pmatrix}\mathbf x+\begin{pmatrix}0\\t\end{pmatrix}.$$

A **linear system** has the form $\mathbf x'=A(t)\mathbf x+\mathbf g(t)$. If every entry of $A$ and $\mathbf g$ is continuous on an interval containing $t_0$, each initial vector $\mathbf x(t_0)$ gives a unique solution throughout that interval.

## Matrices and eigenpairs {#matrices}

Matrix addition is entry by entry. In a product, entry $(i,j)$ is row $i$ of the first matrix dotted with column $j$ of the second. Use row reduction to solve the linear systems below.

1. Solve $\det(A-\lambda I)=0$ for the eigenvalues.
2. For each $\lambda$, row-reduce $(A-\lambda I)\mathbf v=\mathbf0$. Any nonzero vector in this null space is an eigenvector. Nonzero multiples give the same direction.
3. Check $A\mathbf v=\lambda\mathbf v$.

For a $2\times2$ matrix, remember **trace** and **determinant**.

$$A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
\lambda^2-(a+d)\lambda+(ad-bc)=0.$$

### Example · Checking an eigenpair

For $A=\begin{pmatrix}1&1\\6&0\end{pmatrix}$, multiplication gives $A\binom{1}{2}=\binom{3}{6}=3\binom{1}{2}$. Thus $3$ is an eigenvalue and $(1,2)^{\mathsf T}$ is a corresponding eigenvector.

## Real eigenvalues {#real-systems}

For a constant homogeneous system $\mathbf x'=A\mathbf x$, an eigenpair $(r,\mathbf v)$ gives the solution $e^{rt}\mathbf v$. In dimension $n$, combine $n$ independent solutions. If $A$ is a real $2\times2$ matrix with two independent real eigenvectors, the general solution is

$$\mathbf x(t)=C_1e^{r_1t}\mathbf v_1+C_2e^{r_2t}\mathbf v_2.$$

This includes $r=0$, which contributes a constant solution vector. It also works for a repeated real eigenvalue with **two** independent eigenvectors, as for $A=I$. Apply the vector initial condition to solve for the constants.

## Complex conjugate eigenvalues {#complex-systems}

For $\mathbf x'=A\mathbf x$ with $A$ real and constant, compute an eigenvector for **one** eigenvalue in the complex conjugate pair. Write $r=\lambda+i\mu$ and $\mathbf v=\mathbf a+i\mathbf b$. The real and imaginary parts of $e^{rt}\mathbf v$ give two real solutions.

$$\begin{aligned}
\mathbf x_1(t)&=e^{\lambda t}(\mathbf a\cos\mu t-\mathbf b\sin\mu t),\\
\mathbf x_2(t)&=e^{\lambda t}(\mathbf a\sin\mu t+\mathbf b\cos\mu t).
\end{aligned}$$

For a $2\times2$ system, the general real solution is $C_1\mathbf x_1+C_2\mathbf x_2$. For a $3\times3$ system with one real eigenvalue and a complex conjugate pair, add the solution from the real eigenvalue with its own constant. Keep the signs paired with the eigenvalue whose eigenvector you computed.

## Repeated eigenvalues {#repeated-systems}

For $\mathbf x'=A\mathbf x$ with a real constant $2\times2$ matrix, suppose the double eigenvalue $r$ has **one** independent eigenvector $\mathbf v$. Find a generalized eigenvector $\mathbf w$ by solving $(A-rI)\mathbf w=\mathbf v$. The general solution is

$$\mathbf x(t)=C_1e^{rt}\mathbf v+C_2e^{rt}(t\mathbf v+\mathbf w).$$

Keep $t\mathbf v$ and $\mathbf w$ in the **same** solution. Differentiating that solution gives the extra $e^{rt}\mathbf v$ required by $A\mathbf w=r\mathbf w+\mathbf v$.

## Fundamental matrices {#fundamental-matrix}

For $\mathbf{x}'=A(t)\mathbf{x}$, the **Wronskian** of a fundamental set is the determinant of its **fundamental matrix**. Place the $n$ solution vectors **side by side as columns** of $\Phi(t)$, all evaluated at the same $t$.

$$\begin{aligned}
\Phi(t)&=\begin{bmatrix}\mathbf{x}^{(1)}(t)&\cdots&\mathbf{x}^{(n)}(t)\end{bmatrix},\\
W(t)&=\det\Phi(t).
\end{aligned}$$

To test a proposed set of solutions, evaluate $W$ at one point of an interval where $A(t)$ is continuous. If $W(t_0)\ne0$, the columns are linearly independent throughout that interval.

$$\mathbf x(t)=\Phi(t)\mathbf c,\qquad \Phi(t_0)\mathbf c=\mathbf x(t_0).$$

Use the initial data to solve for the constant vector. Equivalently $\mathbf x(t)=\Phi(t)\Phi(t_0)^{-1}\mathbf x(t_0)$.

### Recovering a system from its solution columns

For $\mathbf{x}^{(1)}(t)=(t^2,3t)^{\mathsf T}$ and $\mathbf{x}^{(2)}(t)=(-t^3,2t^2)^{\mathsf T}$, put the first vector in the first column and the second vector in the second column.

$$\begin{aligned}
\Phi(t)&=\begin{bmatrix}t^2&-t^3\\3t&2t^2\end{bmatrix},\\
W(t)&=(t^2)(2t^2)-(-t^3)(3t)=5t^4.
\end{aligned}$$

The pair forms a fundamental set on either interval $t<0$ or $t>0$. To recover the coefficient matrix there, differentiate each column and use $\Phi'=A\Phi$ to obtain $A=\Phi'\Phi^{-1}$.

## Classifying a linear phase portrait {#phase-portraits}

For $\mathbf x'=A\mathbf x$, find the eigenvalues of $A$ and use the table to classify the origin. Name **both** its type and its stability. Order real eigenvalues as $r_1\le r_2$. In the complex rows, $\mu>0$.

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

A **sink** is asymptotically stable. Nearby trajectories approach the equilibrium as $t\to\infty$. A **source** is unstable and nearby trajectories move away. Motion around a **center** is periodic, so nearby solutions stay nearby without converging to the equilibrium.

Real eigenvectors give straight solution lines. At a saddle, solutions on the stable eigenline approach the origin even though the saddle is unstable. For a spiral or center, evaluate $A\mathbf x$ at a convenient point to determine the direction of rotation.
