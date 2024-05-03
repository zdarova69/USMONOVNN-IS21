using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
namespace Test2
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            // Arrange
            int expected = 4;
            int a = 2;
            int b = 2;
            // Act
            int actual = a + b;
            // Assert
            Assert.AreEqual(expected, actual, "Сложение двух положительных чисел не дает правильный результат.");
        }
        [TestMethod]
        public void TestMethod2()
        {
            // Arrange
            int expected = -2;
            int a = 2;
            int b = -4;
            // Act
            int actual = a - b;
            // Assert
            Assert.AreEqual(expected, actual, "Вычитание двух чисел не дает правильный результат.");
        }
    }
}
