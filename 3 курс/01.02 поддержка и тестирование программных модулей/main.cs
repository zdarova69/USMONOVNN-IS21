using System;
using System.Collections.Generic;
using System.Linq;

public class School
{
    public double MinAVG(string[] marks)
    {
        double sum = 0;
        foreach (string mark in marks)
        {
            sum += Convert.ToDouble(mark);
        }
        return Math.Floor(sum / marks.Length);
    }

    public int[] GetCountTruancy(List<Mark> marks)
    {
        int[] counts = new int[marks.Count];
        for (int i = 0; i < marks.Count; i++)
        {
            if (marks[i].Estimation == "прогул")
            {
                counts[i]++;
            }
        }
        return counts;
    }

    public int[] GetCountDisease(List<Mark> marks)
    {
        int[] counts = new int[marks.Count];
        for (int i = 0; i < marks.Count; i++)
        {
            if (marks[i].Estimation == "болезнь")
            {
                counts[i]++;
            }
        }
        return counts;
    }

    public string GetStudNumber(int year, int group, string fio)
    {
        string initials = string.Join("", fio.Split(' ').Select(s => s[0]).ToArray());
        return $"{year}.{group}.{initials}";
    }

    public List<Mark> GetMarks(DateTime now, List<string> students)
    {
        List<Mark> marks = new List<Mark>();
        Random random = new Random();

        foreach (string student in students)
        {
            for (int i = 0; i < 10; i++)
            {
                marks.Add(new Mark
                {
                    Date = now.AddDays(i),
                    Estimation = random.Next(2) == 0 ? "прогул" : random.Next(2) == 0 ? "отсутствие" : random.Next(2) == 0 ? "болезнь" : "оценка"
                });
            }
        }

        return marks;
    }
}

public class Mark
{
    public DateTime Date { get; set; }
    public string Estimation { get; set; }
}
