using DisplayManager.BackGroundServices;
using DisplayManager.Hubs;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
builder.Services.AddSignalR();
builder.Services.AddHostedService<SerialBridgeService>();


var app = builder.Build();

app.UseStaticFiles();
app.UseRouting();


app.MapDefaultControllerRoute();
app.MapHub<SensorsManagerHub>("/SensorsManager");
app.Run();