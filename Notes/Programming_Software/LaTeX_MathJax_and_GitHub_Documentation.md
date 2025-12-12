# Basic Documentation

---

## Table of Contents

1. [Formatting](#formatting)
	1. [Display Math/Chemistry](#display-math-and-chemistry)
	2. [MathJax Supported Environments in GitHub](#mathjax-supported-environments-in-github)
	3. [Inline Math/Chemistry](#inline-math-and-chemistry)
	4. [Automatically Scale Brackets](#automatically-scale-brackets)
2. [Greek Symbols](#greek-symbols)
3. [Math Formatting](#math-formatting)
	1. [Simple Operations and Symbols](#simple-operations-and-symbols)
	2. [Matrices and Vectors](#matrices-and-vectors)
	3. [Systems of Equations with a Matrix](#systems-of-equations-with-a-matrix)
4. [Chemistry Formatting](#chemistry-formatting)
5. [Source](#source)

---

## Formatting

### Display Math and Chemistry

```
$$
\begin{align}
x = 1 & y= 2 & E = m c^{2}\\
z = 3 & z= x + y & D = \frac{m}{v}
\end{align}
$$
```

$$
\begin{align}
x = 1 & y= 2 & E = m c^{2}\\
z = 3 & z= x + y & D = \frac{m}{v}
\end{align}
$$

### MathJax Supported Environments in GitHub

* align
	* align vertically at a specific point (&)
* matrix
* pmatrix
* bmatrix
* Bmatrix
* vmatrix
* Vmatrix
* cases
	* for piecewise functions
	```
	$$
	1+(-1)^n=\begin{cases}
	0, & \text{if $n$ odd}\\
	2, & \text{otherwise}
	\end{cases}
	$$
	```
$$
1+(-1)^n=\begin{cases}
0, & \text{if $n$ odd}\\
2, & \text{otherwise}
\end{cases}
$$
* gather
	* displaying a set of consecutive equations centered horizontally
* multline
	* single equation that needs multiple lines
	* first line left aligned
	* last line right aligned
	* other lines centered

### Inline Math and Chemistry

	This is how you make water $`\ce{2H2(g) + O2(g) -> 2H2O(l)}`$

This is how you make water $`\ce{2H2(g) + O2(g) -> 2H2O(l)}`$

### Automatically Scale Brackets

```$`\left( \frac{a}{b} \right)`$```
	
$`\left( \frac{a}{b} \right)`$

For invisible delimiters (you need both left and right tag for any type of dilimiter)

```$`\left. \frac{d}{dx} \right|`$```

$`\left. \frac{d}{dx} \right|`$

---

## Greek Symbols

| In .md File | Lowercase | In .md File | Uppercase |
| :---: | :---: | :---: | :---: |
| ```$`\alpha`$``` | $`\alpha`$ |   |   |
| ```$`\beta`$``` | $`\beta`$ |   |   |
| ```$`\gamma`$``` | $`\gamma`$ | ```$`\Gamma`$``` | $`\Gamma`$ |
| ```$`\delta`$``` | $`\delta`$ | ```$`\Delta`$``` | $`\Delta`$ |
| ```$`\epsilon`$``` | $`\epsilon`$ |   |   |
| ```$`\zeta`$``` | $`\zeta`$ |   |   |
| ```$`\eta`$``` | $`\eta`$ |   |   |
| ```$`\theta`$``` | $`\theta`$ | ```$`\Theta`$``` | $`\Theta`$ |
| ```$`\iota`$``` | $`\iota`$ |   |   |
| ```$`\kappa`$``` | $`\kappa`$ |   |   |
| ```$`\lambda`$``` | $`\lambda`$ | ```$`\Lambda`$``` | $`\Lambda`$ |
| ```$`\mu`$``` | $`\mu`$ |   |   |
| ```$`\nu`$``` | $`\nu`$ |   |   |
| ```$`\xi`$``` | $`\xi`$ | ```$`\Xi`$``` | $`\Xi`$ |
| ```$`\pi`$``` | $`\pi`$ | ```$`\Pi`$``` | $`\Pi`$ |
| ```$`\rho`$``` | $`\rho`$ |   |   |
| ```$`\sigma`$``` | $`\sigma`$ | ```$`\Sigma`$``` | $`\Sigma`$ |
| ```$`\tau`$``` | $`\tau`$ |   |   |
| ```$`\upsilon`$``` | $`\upsilon`$ | ```$`\Upsilon`$``` | $`\Upsilon`$ |
| ```$`\phi`$``` | $`\phi`$ | ```$`\Phi`$``` | $`\Phi`$ |
| ```$`\chi`$``` | $`\chi`$ |   |   |
| ```$`\psi`$``` | $`\psi`$ | ```$`\Psi`$``` | $`\Psi`$ |
| ```$`\omega`$``` | $`\omega`$ | ```$`\Omega`$``` | $`\Omega`$ |

---

## Math Formatting

### Simple Operations and Symbols

| In .md File | Display |
| :---: | :---: |
| ```$`x^{2}`$``` | $`x^{2}`$ |
| ```$`a_{1}`$``` | $`a_{1}`$ |
| ```$`\frac{a}{b}`$``` | $`\frac{a}{b}`$ |
| ```$`\dfrac{a}{b}`$``` | $`\dfrac{a}{b}`$ |
| ```$`\tfrac{a}{b}`$``` | $`\tfrac{a}{b}`$ |
| ```$`\sqrt{x}`$``` | $`\sqrt{x}`$ |
| ```$`\sqrt[n]{x}`$``` | $`\sqrt[n]{x}`$ |
| ```$`\cdot`$``` | $`\cdot`$ |
| ```$`\times`$``` | $`\times`$ |
| ```$`\div`$``` | $`\div`$ |
| ```$`\infty`$``` | $`\infty`$ |
| ```$`\sum`$``` | $`\sum`$ |
| ```$`\int`$``` | $`\int`$ |
| ```$`\iint`$``` | $`\iint`$ |
| ```$`\iiint`$``` | $`\iiint`$ |
| ```$`\lim`$``` | $`\lim`$ |
| ```$`\max`$``` | $`\max`$ |
| ```$`\min`$``` | $`\min`$ |
| ```$`\log`$``` | $`\log`$ |
| ```$`\ln`$``` | $`\ln`$ |
| ```$`\sin`$``` | $`\sin`$ |
| ```$`\cos`$``` | $`\cos`$ |
| ```$`\tan`$``` | $`\tan`$ |
| ```$`\partial`$``` | $`\partial`$ |
| ```$`\nabla`$``` | $`\nabla`$ |
| ```$`\neq`$``` | $`\neq`$ |
| ```$`\leq`$``` | $`\leq`$ |
| ```$`\geq`$``` | $`\geq`$ |
| ```$`\simeq`$``` | $`\simeq`$ |
| ```$`\approx`$``` | $`\approx`$ |
| ```$`\binom{n}{k}`$``` | $`\binom{n}{k}`$ |
| ```$`\cap`$``` | $`\cap`$ |
| ```$`\cup`$``` | $`\cup`$ |
| ```$`\subset`$``` | $`\subset`$ |
| ```$`\subseteq`$``` | $`\subseteq`$ |
| ```$`\in`$``` | $`\in`$ |
| ```$`\notin`$``` | $`\notin`$ |
| ```$`\forall`$``` | $`\forall`$ |
| ```$`\exists`$``` | $`\exists`$ |
| ```$`\neg`$``` | $`\neg`$ |
| ```$`\emptyset`$``` | $`\emptyset`$ |
| ```$`\hat{x}`$``` | $`\hat{x}`$ |
| ```$`\vec{x}`$``` | $`\vec{x}`$ |
| ```$`\bar{x}`$``` | $`\bar{x}`$ |
| ```$`\tilde{x}`$``` | $`\tilde{x}`$ |
| ```$`\dot{x}`$``` | $`\dot{x}`$ |
| ```$`\ddot{x}`$``` | $`\ddot{x}`$ |
| ```$`\overline{AB}`$``` | $`\overline{AB}`$ |

### Matrices and Vectors

```
$$
\begin{matrixtype}
a & b \\
c & d \\
e & f
\end{matrixtype}
$$
```

| matrixtype | Displayed |
| :---: | :---: |
| matrix | $`\begin{matrix} a & b \\ c & d \\ e & f \end{matrix}`$ |
| pmatrix | $`\begin{pmatrix} a & b \\ c & d \\ e & f \end{pmatrix}`$ |
| bmatrix | $`\begin{bmatrix} a & b \\ c & d \\ e & f \end{bmatrix}`$ |
| Bmatrix | $`\begin{Bmatrix} a & b \\ c & d \\ e & f \end{Bmatrix}`$ |
| vmatrix | $`\begin{vmatrix} a & b \\ c & d \\ e & f \end{vmatrix}`$ |
| Vmatrix | $`\begin{Vmatrix} a & b \\ c & d \\ e & f \end{Vmatrix}`$ |

```
$$
\begin{bmatrix}
1 & 2 & \cdots & n \\
\vdots & \vdots & \ddots & \vdots \\
1 & 2 & \cdots & n
\end{bmatrix}
$$ 
```

$$
\begin{bmatrix}
1 & 2 & \cdots & n \\
\vdots & \vdots & \ddots & \vdots \\
1 & 2 & \cdots & n
\end{bmatrix}
$$ 

### Systems of Equations with a Matrix

```
$$
\left[\begin{matrix} 3x & -2y \\
x & +y\end{matrix}\right|\left.\begin{matrix} 6 \\
-8 \end{matrix}\right] 
$$
```

$$
\left[\begin{matrix} 3x & -2y \\
x & +y\end{matrix}\right|\left.\begin{matrix} 6 \\
-8 \end{matrix}\right] 
$$

---

## Chemistry Formatting

| In .md File | Bond |
| :---: | :---: |
| ```$`\ce{A-B}`$``` | $`\ce{A-B}`$ |
| ```$`\ce{A=B}`$``` | $`\ce{A=B}`$ |
| ```$`\ce{A#B}`$``` | $`\ce{A#B}`$ |

| In .md File | Arrows |
| :---: | :---: |
| ```$`\ce{A -> B}`$``` | $`\ce{A -> B}`$ |
| ```$`\ce{A <=> B}`$``` | $`\ce{A <=> B}`$ |
| ```$`\ce{A <-> B}`$``` | $`\ce{A <-> B}`$ |
| ```$`\ce{A ->[heat] B}`$``` | $`\ce{A ->[heat] B}`$ |
| ```$`\ce{A ->[hv][Pt] B}`$``` | $`\ce{A ->[hv][Pt] B}`$ |

Charges: ```$`\ce[SO4^{2-}}`$```

Radicals: ```$`\ce{Cl.}`$```

Units: ```$`\pu{5.0 ^{\circ} C}`$```

---

## Source

MathJax: <https://docs.mathjax.org/en/latest/>

---