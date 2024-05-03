using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
namespace UnitTestPro2
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            // Arrange
            int expected = 5;
            int actual;
            // Act
            actual = SomeClass.MethodToTest();
            // Assert
            Assert.AreEqual(expected, actual);
        }
    }
    public class SomeClass
    {
        public static int MethodToTest()
        {
            // Example method to be tested
            return 5;
        }
    }
}
