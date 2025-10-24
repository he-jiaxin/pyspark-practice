#!/usr/bin/env python3

import os
# Set Java 11 explicitly
os.environ['JAVA_HOME'] = '/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home'

# Remove the security manager configuration that's causing issues

print(f"JAVA_HOME set to: {os.environ['JAVA_HOME']}")

try:
    from pyspark.sql import SparkSession
    print("PySpark imported successfully")
    
    spark = SparkSession.builder.appName('Test').getOrCreate()
    print("Spark session created successfully!")
    
    # Test with a simple operation
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    columns = ["name", "age"]
    df = spark.createDataFrame(data, columns)
    df.show()
    
    spark.stop()
    print("Test completed successfully!")
    
except Exception as e:
    print(f"Error: {e}")