// Program.cs
using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace DonorSearchExample
{
    class Program
    {
        // Entry point compatible with older language versions
        static void Main(string[] args)
        {
            RunAsync(args).GetAwaiter().GetResult();
        }

        static async Task RunAsync(string[] args)
        {
            if (args.Length < 2)
            {
                Console.WriteLine("Usage: dotnet run <requestKey> <emailAddress>");
                return;
            }

            string requestKey = args[0];       // untrusted
            string emailAddress = args[1];     // untrusted

            // ----- Mirrors your DonorAPI.cs -----
            string filter = "{" + requestKey + ":'" + emailAddress + "'}";
            Console.WriteLine("Filter: " + filter);

            // ----- Mirrors your DonorProvider.cs -----
            string endpointCustomer = string.Format(
                "https://api.example.com/v1.3/search?q={0}",
                filter);   // tainted data inserted into query parameter

            Console.WriteLine("Calling: " + endpointCustomer);

            // Classic using-statement instead of C# 8 "using var"
            using (var client = new HttpClient())
            {
                try
                {
                    // This call should be considered the "sink" for tainted data
                    HttpResponseMessage response =
                        await client.GetAsync(endpointCustomer);

                    string body = await response.Content.ReadAsStringAsync();
                    Console.WriteLine("Response received (length): " + body.Length);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Error during request: " + ex.Message);
                }
            }
        }
    }
}
