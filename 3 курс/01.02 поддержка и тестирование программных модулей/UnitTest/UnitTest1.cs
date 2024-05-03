using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
namespace UnitTest
{
    [TestClass]
    public class UnitTest1
    {
        private int[] GenerateRandomArray(int length)
        {
            Random random = new Random();
            int[] array = new int[length];
            for (int i = 0; i < length; i++)
            {
                array[i] = random.Next();
            }
            return array;
        }
        [TestMethod]
        public void TestArraySort()
        {
            // Arrange
            int[] array = GenerateRandomArray(1000);
            int[] expected = (int[])array.Clone();
            Array.Sort(expected);
            // Act
            // You can put the code you want to test here. For example:
            // YourClass.SortArray(array);
            // Assert
            CollectionAssert.AreEqual(expected, array);
        }
        [TestMethod]
        public void TestArraySortWithEmptyArray()
        {
            // Arrange
            int[] array = new int[0];
            int[] expected = new int[0];
            // Act
            // You can put the code you want to test here. For example:
            // YourClass.SortArray(array);
            // Assert
            CollectionAssert.AreEqual(expected, array);
        }
        [TestMethod]
        public void TestArraySortWithSingleElement()
        {
            // Arrange
            int[] array = { 5 };
            int[] expected = { 5 };
            // Act
            // You can put the code you want to test here. For example:
            // YourClass.SortArray(array);
            // Assert
            CollectionAssert.AreEqual(expected, array);
        }
        // You can add more meaningful test methods as needed
    }
}
