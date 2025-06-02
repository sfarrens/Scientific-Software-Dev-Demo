#!/usr/bin/env python3
"""
Profiling script for mycosmo package.
Demonstrates different profiling approaches for scientific computing code.
"""

import timeit
import cProfile
import pstats
import io
import sys
from datetime import datetime
from line_profiler import LineProfiler
from memory_profiler import profile
import numpy as np
from mycosmo import cosmology

def save_results(filename, content):
    """Save profiling results to a file."""
    with open(filename, 'w') as f:
        f.write(content)

def profile_with_timeit():
    """Basic timing using timeit."""
    print("\n=== Timeit Profiling ===")
    results = []
    
    # Example timing of cosmology functions
    setup = """
from mycosmo import cosmology
cosmo_dict = {"H0": 70, "omega_m_0": 0.3, "omega_k_0": 0.0, "omega_lambda_0": 0.7}
redshift = 0.0
"""
    # Time hubble function
    stmt = "cosmology.hubble(redshift, cosmo_dict)"
    number = 1000
    time = timeit.timeit(stmt, setup, number=number)
    result = f"hubble() average time per call: {time/number:.6f} seconds"
    print(result)
    results.append(result)
    
    # Time critical_density function
    stmt = "cosmology.critical_density(redshift, cosmo_dict)"
    time = timeit.timeit(stmt, setup, number=number)
    result = f"critical_density() average time per call: {time/number:.6f} seconds"
    print(result)
    results.append(result)
    
    # Save results
    save_results('timeit_results.log', '\n'.join(results))

def profile_with_cprofile():
    """Function-level profiling using cProfile."""
    print("\n=== cProfile Profiling ===")
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Run cosmology calculations
    cosmo_dict = {"H0": 70, "omega_m_0": 0.3, "omega_k_0": 0.0, "omega_lambda_0": 0.7}
    redshifts = np.linspace(0, 10, 1000)
    
    # Profile both functions
    hubble_values = cosmology.hubble(redshifts, cosmo_dict)
    density_values = cosmology.critical_density(redshifts, cosmo_dict)
    
    profiler.disable()
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(20)  # Print top 20 functions
    results = s.getvalue()
    print(results)
    
    # Save results
    save_results('cprofile_results.prof', results)
    # Also save in a more readable format
    save_results('cprofile_results.log', results)

def profile_with_line_profiler():
    """Line-by-line profiling using line_profiler."""
    print("\n=== Line Profiler ===")
    profiler = LineProfiler()
    
    # Add the functions we want to profile
    profiler.add_function(cosmology.hubble)
    profiler.add_function(cosmology.critical_density)
    
    # Run the code
    profiler.enable()
    cosmo_dict = {"H0": 70, "omega_m_0": 0.3, "omega_k_0": 0.0, "omega_lambda_0": 0.7}
    redshifts = np.linspace(0, 10, 1000)
    hubble_values = cosmology.hubble(redshifts, cosmo_dict)
    density_values = cosmology.critical_density(redshifts, cosmo_dict)
    profiler.disable()
    
    # Capture and save results
    s = io.StringIO()
    profiler.print_stats(stream=s)
    results = s.getvalue()
    print(results)
    
    # Save results
    save_results('line_profiler_results.lprof', results)
    # Also save in a more readable format
    save_results('line_profiler_results.log', results)

@profile
def profile_memory_usage():
    """Memory profiling using memory_profiler."""
    print("\n=== Memory Profiling ===")
    cosmo_dict = {"H0": 70, "omega_m_0": 0.3, "omega_k_0": 0.0, "omega_lambda_0": 0.7}
    redshifts = np.linspace(0, 10, 1000)
    
    # Calculate values
    hubble_values = cosmology.hubble(redshifts, cosmo_dict)
    density_values = cosmology.critical_density(redshifts, cosmo_dict)
    
    return hubble_values, density_values

def main():
    """Run all profiling approaches."""
    print("Starting profiling of mycosmo package...")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Python version: {sys.version}")
    print(f"NumPy version: {np.__version__}")
    print("\nSystem Information:")
    print(f"OS: {sys.platform}")
    
    # Run different profiling approaches
    profile_with_timeit()
    profile_with_cprofile()
    profile_with_line_profiler()
    profile_memory_usage()

if __name__ == "__main__":
    main() 