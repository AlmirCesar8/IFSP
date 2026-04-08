package PadraoSingleton_SimpleFactory;

interface Logger {
    void log(String msg);
}

class ConsoleLogger implements Logger {
    @Override
    public void log(String msg) {
        System.out.println(msg);
    }
}
 class FileLogger implements Logger {
     @Override
     public void log(String msg) {
         System.out.println("olha que arquivo bonito " + msg);
     }
 }

