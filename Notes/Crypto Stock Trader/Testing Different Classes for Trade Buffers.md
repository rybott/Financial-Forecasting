```python
import timeit

import pandas as pd

  

# Global variable setup

BUFFER_SIZE = 15

buffer_global = [None] * BUFFER_SIZE

  

def append_to_global(data):

    buffer_global.append(data)

    buffer_global.pop(0)

  

# Class variable setup

class CircularBuffer:                               # ChatGPT Class Type  
    def __init__(self, size):
        self.size = size
        self.buffer = pd.DataFrame(index=range(size), columns=["timestamp", "price", "volume"])  # Adjust columns as needed
        self.index = 0
        
    def append(self, data):
        # Convert trade to pandas Series
        trade_series = pd.Series(data)
        # Place new trade in the current index position
        self.buffer.iloc[self.index] = trade_series
        # Update index in a circular manner
        self.index = (self.index + 1) % self.size


  

class OP_CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = pd.DataFrame(columns=["timestamp", "price", "volume"])  # Adjust columns as needed

    def append(self, data):
        # Convert trade to pandas Series
        trade_series = pd.Series(data, index=self.buffer.columns)
        if len(self.buffer) == 15:
            self.buffer = self.buffer.shift(-1)
            self.buffer.iloc[-1] = trade_series
        elif len(self.buffer) < 15:
            self.buffer = pd.concat([self.buffer, trade_series.to_frame().T], ignore_index=True)
        else:
            print(f"Tade Buffer Error - Buffer size {len(self.buffer)}")

  
  

buffer_class = CircularBuffer(size=15)

OPbuff_class = OP_CircularBuffer(size=15)

  

# Benchmark global variable

def benchmark_global():

    for i in range(100):

        append_to_global(i)

  

# Benchmark class variable

def benchmark_class():

    for i in range(100):

        i = {"timestamp": 1, "price":2, "volume":3}

        buffer_class.append(i)

  

def OPbenchmark_class():

    for i in range(100):

        i = {"timestamp": 1, "price":2, "volume":3}

        OPbuff_class.append(i)

  

# Run benchmarks

time_global = timeit.timeit(benchmark_global, number=1000)

print(f"Global variable time: {time_global}")

time_class = timeit.timeit(benchmark_class, number=1000)

print(f"Class variable time: {time_class}")

OPtime_class = timeit.timeit(OPbenchmark_class, number=1000)

print(f"OP Class variable time: {OPtime_class}")
```