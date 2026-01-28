import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, units="us")
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
    assert dut.uo_out[0].value == 0
    assert dut.uo_out[1].value == 0

    # ---- Test case 2: A=0 B=0 Cin=1
    dut.ui_in.value = 0b001
    await ClockCycles(dut.clk, 10)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 0

    # ---- Test case 3: A=0 B=1 Cin=0
    dut.ui_in.value = 0b010
    await ClockCycles(dut.clk, 10)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 0
