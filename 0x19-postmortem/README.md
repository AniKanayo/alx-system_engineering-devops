![Postmortem](https://twitter.com/devopsreact/status/834887829486399488)
Issue Summary:
Duration: 3 hours (from 09:00 AM - 12:00 PM GMT+1)
Impact: Our website users had a difficult time in accessing our website and mobile application.
Roughly 70% of the users experienced that difficulty. 
Root Cause: An unanticipated traffic surge led to the crashing of the web server which resulted in service downtime.

Timeline:
$	9:00 AM: Our web server monitoring system raised an alarm showing that the website and mobile application have fallen below their operational thresholds. 
$	9:15 AM: Our engineer was informed about the ugly development and he started investigating the issue. 
$	9:30 AM: The engineer observed that the web server had crashed and he tried restarting it, but to no avail.
§	9:40 AM: We have to involve the database team to ascertain the functionality status of the database.
§	10:00 AM: Our network team was also involved to check any network-related issues that may have caused the crashing.
§	10:15 AM: The findings showed that a sudden surge in traffic led the web server to crash.
§	10:40 AM: The traffic surge was link to a campaign promo of a new product that had suddenly gone viral.
§	11:15 AM: The team decided to temporarily redirect the traffic to a backup server while the main server was being repaired.
§	11:30 AM: The main server came back to its operational status, and the traffic was smoothly redirected back to it
§	12:00 PM: The website and mobile application were fully operational again.

Root Cause and Resolution: 
The root cause of the issue was a sudden increase in traffic that caused the web server to break down.
The surge in traffic was traced to a campaign promo that had suddenly gone viral.

To forestall a similar occurrence in the future, these corrective and preventative measures below will be implemented.
§	Additional capacity will be added to the web server to address unexpected rise in traffic.
§	An improved monitoring strategy to detect increase in traffic before it causes an outage.
§	Optimize the website and mobile application to reduce server load.
§	Review the campaign promo process to ensure that it can handle sudden traffic surges.

Corrective and Preventative Measures:
§	Providing additional web server resources to the server.
§	Execute improved traffic monitoring and alerting strategy to detect and attend to traffic surges in a timely manner.
§	To optimize the website and mobile application to minimize server load, such as caching and optimizing database queries.
§	To review the campaign promo process to ensure that it can manage sudden rise in traffic, such as load testing and capacity planning.

In conclusion, the downtime was caused by a sudden increase in traffic that over-laboured the web server, giving rise to website and mobile application being unavailable for approximately 3 hours. The issue was resolved by redirecting traffic to a backup server while the main server was being fixed. To prevent similar occurrence in the future, we will implement various corrective and preventative measures to increase server capacity, improve monitoring, optimize the website and mobile application and review the campaign promo process.

