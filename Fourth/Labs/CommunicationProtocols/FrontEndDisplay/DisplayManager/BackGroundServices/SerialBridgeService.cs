using System.Diagnostics;
using System.IO.Ports;
using DisplayManager.Clients;
using DisplayManager.Hubs;
using Microsoft.AspNetCore.SignalR;

namespace DisplayManager.BackGroundServices;

public class SerialBridgeService : BackgroundService{
    private readonly IHubContext<SensorsManagerHub, ISensorsManagerClient> _hubContext;
    
    private SerialPort? _serialPort;
    private readonly string _pty = "/tmp/vterm1";

    private Process? _socatProcess;
    private readonly string _socatPath;
    public SerialBridgeService(
        IHubContext<SensorsManagerHub, ISensorsManagerClient> hubContext,
        IWebHostEnvironment environment
    ){
        _hubContext = hubContext;

        _socatPath = $"{environment.ContentRootPath}/Properties/start_socat.sh";

    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        try
        {

            var startInfo = new ProcessStartInfo
            {
                FileName = "/bin/bash",
                Arguments = _socatPath,
                UseShellExecute = false,
                RedirectStandardOutput = false,
                RedirectStandardError = false,
                CreateNoWindow = true
            };

            _socatProcess = Process.Start(startInfo);

            Console.WriteLine("Starting socat tunnel...");

            int retries = 50;
            while(!File.Exists(_pty) && retries-- > 0 && !stoppingToken.IsCancellationRequested)
                await Task.Delay(100,stoppingToken);

            Console.WriteLine($"PTY ready at {_pty}");

            _serialPort = new SerialPort(_pty, 9600);

            _serialPort.Open();


            var reader = new StreamReader(_serialPort.BaseStream);

            Console.WriteLine("SerialBridgeService started.");

            while(!stoppingToken.IsCancellationRequested){
                if(_serialPort.BytesToRead > 0){
                    string? time = reader.ReadLine();
                    string? temp = reader.ReadLine();

                    if(!string.IsNullOrEmpty(time) && !string.IsNullOrEmpty(temp))
                    {
                        await _hubContext.Clients.All.ReadSensorsData(time, temp);
                    }

                }
                else
                {
                    await Task.Delay(100, stoppingToken);
                }
            }
        }
        catch(Exception ex)
        {
            Console.WriteLine($"SerialBridgeService error: {ex}");
        }
    }

    public override async Task StopAsync(CancellationToken cancellationToken)
    {

        Console.WriteLine("Stopping SerialBridgeService...");


        if(_serialPort != null && _serialPort.IsOpen){
            _serialPort.Close();
            _serialPort.Dispose();
        }

        
        if(_socatProcess != null && !_socatProcess.HasExited){
            try
            {
                _socatProcess.Kill();
            }
            catch
            {
                Console.WriteLine("Can't kill Socat!");
            }

            _socatProcess.Dispose();
        }

        await base.StopAsync(cancellationToken);
    }
}