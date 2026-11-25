## Homogeneous plus particular {#particular}

In a linear equation $L[y]=g(t)$, first solve $L[y_h]=0$, then find **one** particular solution $Y$ of $L[Y]=g$. The general solution is

$$y=y_h+Y.$$

Apply initial conditions to the **sum**, including its derivatives.

## Undetermined coefficients {#undetermined}

Use this method for **constant coefficients** and a forcing built from polynomials, exponentials, sines, cosines, or their sums and products.

| Forcing | Start with this trial |
|:---|:---|
| Polynomial of degree $n$ | A general polynomial $A_nt^n+\cdots+A_1t+A_0$ |
| $e^{at}$ | $Ae^{at}$ |
| $\sin(bt)$ or $\cos(bt)$ | $A\cos(bt)+B\sin(bt)$ |
| A degree-$n$ polynomial times $\sin(bt)$ or $\cos(bt)$ | $Q_n(t)\cos(bt)+R_n(t)\sin(bt)$, using two full degree-$n$ polynomial trials with independent coefficients |

**Check for overlap with $y_h$.** For each forcing block, multiply its whole trial by $t$ until its terms are independent of the homogeneous solutions. Equivalently, multiply by $t^s$ if the corresponding characteristic root has multiplicity $s$. Substitute the trial, collect like terms, and solve for its coefficients.

### Recognizing resonance

For $y''-y=e^t$, the homogeneous solutions are $e^t,e^{-t}$. An $Ae^t$ trial would disappear on substitution, so try $Y=Ate^t$.

For $y''-3y'+2y=te^{2t}$, first write $(At+B)e^{2t}$. Since $2$ is a simple characteristic root, use $t(At+B)e^{2t}$. In a **trial-form** question, stop once the independent trial is specified.

## Variation of parameters {#variation}

Use this for a linear nonhomogeneous equation with known homogeneous solutions, including variable-coefficient equations and forcings that do not fit the trial table. **Normalize first**, dividing every term by the coefficient of $y''$.

$$y''+p(t)y'+q(t)y=g(t),\qquad W=y_1y_2'-y_1'y_2.$$

Choose a **fundamental set** $\{y_1,y_2\}$ for the homogeneous equation on the interval of interest, so $W\ne0$. Let $Y=u_1y_1+u_2y_2$. Solving $u_1'y_1+u_2'y_2=0$ and $u_1'y_1'+u_2'y_2'=g$ gives

$$u_1'=-\frac{y_2g}{W},\qquad u_2'=\frac{y_1g}{W}.$$

Integrate, multiply by the corresponding homogeneous solutions, and add.

$$Y=-y_1\int\frac{y_2g}{W}\,dt+y_2\int\frac{y_1g}{W}\,dt.$$

Use the **normalized** $g$ in both integrals. Integration constants here only reproduce terms already in $y_h$.
