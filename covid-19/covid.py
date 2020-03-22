import math
import matplotlib.pyplot as plt
import numpy as np

class COVIDmodel:
  N: float
  Io: int
  K: float
  quarantine: bool
  time: np.ndarray
  infected: list

  def __init__(self, N, Io, tn, In, time, quarantine=False):
    self.N = N
    self.Io = Io
    self.time = time
    self.infected = []
    self.quarantine = quarantine
    self._calculate_propagation_rate(tn, In)
    self._propagate_virus()

  def _calculate_propagation_rate(self, tn, In):
    self.K = -(1 / (tn * N)) * math.log((Io / (N * In)) * (N - In))
    if self.quarantine:
      self.K = self.K / 2

  def I(self, t):
    denominator = (1.0 + (self.N / self.Io) * math.exp(-self.N * self.K * t))
    return self.N / denominator

  def _propagate_virus(self):
    for t in time:
      self.infected.append(math.ceil(self.I(t)))

  def get_infected(self):
    return self.infected

  def plot_results(self):
    color = "red" if not self.quarantine else "green"
    label = "without quarantine" if not self.quarantine else "with quarantine"
    plt.plot(self.time, self.infected, color=color, label=label)
    plt.xlabel("time (days)")
    plt.ylabel("infected (people)")
    plt.ylim(0, 10000)




N = 49.07e6 #colombian population
Io = 1 #patient zero
tn = 16 #sixteenth day
In = 210 #infected when t=16
time = np.linspace(1, 50, num=50)
without_quarantine = COVIDmodel(N, Io, tn, In, time, quarantine=False) 
with_quarantine = COVIDmodel(N, Io, tn, In, time, quarantine=True)
without_quarantine.plot_results()
with_quarantine.plot_results()
plt.plot([tn], [In], marker='o', markersize=5, color="blue", label="we are here")
plt.legend()
plt.title("Infected vs Time - COVID-19")
plt.grid(linestyle='-', linewidth=1)
plt.show()
