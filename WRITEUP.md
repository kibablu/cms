# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

I chose webapp(App Service) over a VM and here are my reasons:
- On analyzing cost, webapps are cheaper for lightweight apps compared to vms as webapps you're being billed for the service plane, while vm you're being billed for resources allocated. _(even no resources are running)_
- Scaling our app on webapp is handled by azure, unlike on a vm where we will have to provision extra hardware and configure it. _(time consumming and cost)_
- VMs are most likly to fail as the app gets more traffic(not enough resources), while app service could be available as it scale automatically.
- App service are easier to manage and deploy your code, unlike Vm where you will have to configure the hardaware, OS and the dependencies of your app.
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

As the bussiness is booming, App service will not be a suitable solution following these reasons:
- I want to have full control of the OS, as VM _(IaaS)_ you have total control of the OS compared to App Service _(PaaS)_.
- App Service has a limit of CPUs and memory allocated, I will chose VM to have more compute and memory option for scalabilty.
- Having apps with different dependencies and language, webapp is not suitable for this, hence Vms will be  good fit for these kind of workloads.
- Vms are good and easier for testing our different apps compared to webapps that have language and runtime constraints.

[Live cms on azure App Service](https://projectcms.azurewebsites.net) 
