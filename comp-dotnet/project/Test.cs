// Test.cs
using System;
using System.Net.Http;

namespace DonorSearchExample
{
    // This class mirrors your DonorAPI/DonorProvider pattern
    public class DonorSearch
    {
        // This method is what Sonar should flag
        public void VulnerableSearch(string requestKey, string emailAddress)
        {
            // ----- Mirrors your DonorAPI.cs -----
            string filter = "{" + requestKey + ":'" + emailAddress + "'}";
            Console.WriteLine("Filter: " + filter);

            // ----- Mirrors your DonorProvider.cs -----
            string endpointCustomer = string.Format(
                "https://api.example.com/v1.3/search?q={0}",
                filter);   // tainted data inserted into query parameter

            Console.WriteLine("Calling: " + endpointCustomer);

            // Classic using-statement, compatible with C# 7.3
            using (var client = new HttpClient())
            {
                try
                {
                    // This call is the "sink" for the tainted data
                    HttpResponseMessage response =
                        client.GetAsync(endpointCustomer).Result;

                    string body = response.Content.ReadAsStringAsync().Result;
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
