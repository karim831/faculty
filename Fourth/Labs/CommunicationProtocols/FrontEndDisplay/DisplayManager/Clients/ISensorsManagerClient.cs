namespace DisplayManager.Clients;

public interface ISensorsManagerClient{
     Task ReadSensorsData(string time, string temp);
}