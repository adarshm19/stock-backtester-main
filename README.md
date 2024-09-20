# Trading Strategy Backtesting Project

## Overview

This project implements and backtests various trading strategies using Python, `pandas`, and `yfinance`. The primary objective is to analyze the performance of different strategies by generating buy and sell signals based on specific conditions and evaluating the resulting profit or loss. The project also generates comprehensive reports in Excel format to summarize the backtesting results.

## Features

- **Moving Average Strategy:**
  - Generates buy and sell signals based on the crossover of short-term and long-term Simple Moving Averages (SMAs).
  - Simulates trades and calculates the final portfolio value and profit/loss.
  - Outputs an Excel report with trade logs and an equity curve.

- **Percentage Change Strategy:**
  - Generates buy signals when today's price is lower than the previous day's price by a certain percentage.
  - Generates sell signals when today's price is higher than the previous day's price by a certain percentage.
  - Simulates trades using a specified portion of available cash and calculates the final portfolio value and profit/loss.
  - Outputs an Excel report similar to the moving average strategy.

- **Excel Reporting:**
  - The project generates detailed Excel reports containing:
    - A summary of initial capital, final portfolio value, and total profit/loss.
    - A log of all trades made during the backtesting period.
    - An equity curve showing the portfolio's value over time.

- **You can add your own strategy and use the back tester to test it.**
