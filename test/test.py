import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

def bit(x, n):
    return (x >> n) & 1

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")  # 'unit' avoids warning
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # ---- Test case 1: A=0 B=0 Cin=0
    dut.ui_in.value = 0b000
    await ClockCycles(dut.clk, 10)
    out = int(dut.uo_out.value)
    assert bit(out, 0) == 0
    assert bit(out, 1) == 0

    # ---- Test case 2: A=0 B=0 Cin=1
    dut.ui_in.value = 0b001
    await ClockCycles(dut.clk, 10)
    out = int(dut.uo_out.value)
    assert bit(out, 0) == 1
    assert bit(out, 1) == 0

    # ---- Test case 3: A=0 B=1 Cin=0
    dut.ui_in.value = 0b010
    await ClockCycles(dut.clk, 10)
    out = int(dut.uo_out.value)
    assert bit(out, 0) == 1
    assert bit(out, 1) == 0
