using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prog1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] x = new int[] { 1, 5, 112, 3, 7 };
            int m = mayorElemento(x);

            Console.WriteLine(m);
            Console.Read();
        }

        private static int mayorElemento(int[] x)
        {
            int max = 0;

            for (int i = 0; i < 5; i++)
            {
                if (x[i] > max)
                    max = x[i];
            }
            return max;
        }
    }
}
