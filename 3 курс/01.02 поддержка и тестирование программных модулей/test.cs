using Xunit;
using System;
using System.Collections.Generic;

public class SchoolTests
{
    [Fact]
    public void MinAVG_ShouldCalculateCorrectly()
    {
        School school = new School();
        string[] marks = { "5", "4", "3", "2", "3" };

        double result = school.MinAVG(marks);

        Assert.Equal(3, result);
    }

    [Fact]
    public void MinAVG_ShouldHandleEmptyArray()
    {
        School school = new School();
        string[] marks = { };

        double result = school.MinAVG(marks);

        Assert.Equal(0, result);
    }

    [Fact]
    public void GetCountTruancy_ShouldReturnCorrectCounts()
    {
        School school = new School();
        List<Mark> marks = new List<Mark>
        {
            new Mark { Date = DateTime.Now, Estimation = "прогул" },
            new Mark { Date = DateTime.Now, Estimation = "оценка" },
            new Mark { Date = DateTime.Now, Estimation = "прогул" }
        };

        int[] result = school.GetCountTruancy(marks);

        Assert.Equal(0, result[0]);
        Assert.Equal(1, result[1]);
        Assert.Equal(0, result[2]);
    }

    [Fact]
    public void GetCountDisease_ShouldReturnCorrectCounts()
    {
        School school = new School();
        List<Mark> marks = new List<Mark>
        {
            new Mark { Date = DateTime.Now, Estimation = "болезнь" },
            new Mark { Date = DateTime.Now, Estimation = "оценка" },
            new Mark { Date = DateTime.Now, Estimation = "болезнь" }
        };

        int[] result = school.GetCountDisease(marks);

        Assert.Equal(1, result[0]);
        Assert.Equal(0, result[1]);
        Assert.Equal(1, result[2]);
    }
}