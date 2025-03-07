#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

// Clase para representar un paquete
class Paquete {
public:
    string id;
    double peso;
    string categoria; // elemental, regular, volumétrico
    string descripcion;

    Paquete(string id, double peso, string categoria, string descripcion)
        : id(id), peso(peso), categoria(categoria), descripcion(descripcion) {}

    void mostrarInfo() {
        cout << "Paquete ID: " << id << ", Peso: " << peso << " kg, Categoría: " << categoria
             << ", Descripción: " << descripcion << endl;
    }
};

// Clase para representar un envío
class Envio {
public:
    string id;
    string destinatario;
    vector<Paquete> paquetes;
    string estado; // En tránsito, Entregado, etc.

    Envio(string id, string destinatario) : id(id), destinatario(destinatario), estado("En tránsito") {}

    void agregarPaquete(Paquete paquete) {
        paquetes.push_back(paquete);
    }

    void mostrarInfo() {
        cout << "Envío ID: " << id << ", Destinatario: " << destinatario << ", Estado: " << estado << endl;
        cout << "Paquetes en este envío:" << endl;
        for (auto& paquete : paquetes) {
            paquete.mostrarInfo();
        }
    }

    void actualizarEstado(string nuevoEstado) {
        estado = nuevoEstado;
        cout << "Estado del envío " << id << " actualizado a: " << estado << endl;
    }
};

// Clase para gestionar usuarios
class Usuario {
public:
    string username;
    string password;

    // Constructor por defecto
    Usuario() : username(""), password("") {}

    // Constructor con parámetros
    Usuario(string username, string password) : username(username), password(password) {}

    bool autenticar(string inputPassword) {
        return password == inputPassword;
    }
};

// Clase principal del sistema
class SistemaLogistica {
private:
    vector<Paquete> paquetes;
    vector<Envio> envios;
    map<string, Usuario> usuarios; // Mapa para almacenar usuarios registrados

public:
    // Registrar un nuevo paquete
    void registrarPaquete() {
        string id, categoria, descripcion;
        double peso;

        cout << "Ingrese el ID del paquete: ";
        cin >> id;
        cout << "Ingrese el peso del paquete (kg): ";
        cin >> peso;
        cout << "Ingrese la categoría (elemental, regular, volumétrico): ";
        cin >> categoria;
        cout << "Ingrese la descripción del paquete: ";
        cin.ignore(); // Para limpiar el buffer
        getline(cin, descripcion);

        Paquete nuevoPaquete(id, peso, categoria, descripcion);
        paquetes.push_back(nuevoPaquete);
        cout << "Paquete registrado exitosamente." << endl;
    }

    // Crear un nuevo envío
    void crearEnvio() {
        string id, destinatario;

        cout << "Ingrese el ID del envío: ";
        cin >> id;
        cout << "Ingrese el nombre del destinatario: ";
        cin.ignore(); // Para limpiar el buffer
        getline(cin, destinatario);

        Envio nuevoEnvio(id, destinatario);
        envios.push_back(nuevoEnvio);
        cout << "Envío creado exitosamente." << endl;
    }

    // Agregar un paquete a un envío existente
    void agregarPaqueteAEnvio() {
        string idEnvio, idPaquete;
        cout << "Ingrese el ID del envío: ";
        cin >> idEnvio;
        cout << "Ingrese el ID del paquete: ";
        cin >> idPaquete;

        // Buscar el paquete
        Paquete* paqueteEncontrado = nullptr;
        for (auto& paquete : paquetes) {
            if (paquete.id == idPaquete) {
                paqueteEncontrado = &paquete;
                break;
            }
        }

        if (paqueteEncontrado) {
            // Buscar el envío
            for (auto& envio : envios) {
                if (envio.id == idEnvio) {
                    envio.agregarPaquete(*paqueteEncontrado);
                    cout << "Paquete agregado al envío " << idEnvio << endl;
                    return;
                }
            }
            cout << "Envío no encontrado." << endl;
        } else {
            cout << "Paquete no encontrado." << endl;
        }
    }

    // Mostrar información de todos los envíos
    void mostrarEnvios() {
        if (envios.empty()) {
            cout << "No hay envíos registrados." << endl;
        } else {
            for (auto& envio : envios) {
                envio.mostrarInfo();
            }
        }
    }

    // Registrar un nuevo usuario
    void registrarUsuario() {
        string username, password;

        cout << "Ingrese el nombre de usuario: ";
        cin >> username;
        cout << "Ingrese la contraseña: ";
        cin >> password;

        usuarios[username] = Usuario(username, password);
        cout << "Usuario registrado exitosamente." << endl;
    }

    // Autenticar un usuario
    bool autenticarUsuario() {
        string username, password;

        cout << "Ingrese el nombre de usuario: ";
        cin >> username;
        cout << "Ingrese la contraseña: ";
        cin >> password;

        if (usuarios.find(username) != usuarios.end()) {
            if (usuarios[username].autenticar(password)) {
                cout << "Autenticación exitosa." << endl;
                return true;
            }
        }
        cout << "Autenticación fallida." << endl;
        return false;
    }
};

// Función para mostrar el menú
void mostrarMenu() {
    cout << "\n--- Menú de Sistema de Logística ---" << endl;
    cout << "1. Registrar usuario" << endl;
    cout << "2. Autenticar usuario" << endl;
    cout << "3. Registrar paquete" << endl;
    cout << "4. Crear envío" << endl;
    cout << "5. Agregar paquete a envío" << endl;
    cout << "6. Mostrar envíos" << endl;
    cout << "7. Salir" << endl;
    cout << "Seleccione una opción: ";
}

// Función principal
int main() {
    SistemaLogistica sistema;
    int opcion;

    do {
        mostrarMenu();
        cin >> opcion;

        switch (opcion) {
            case 1:
                sistema.registrarUsuario();
                break;
            case 2:
                if (sistema.autenticarUsuario()) {
                    // Si la autenticación es exitosa, continuar con las operaciones
                }
                break;
            case 3:
                sistema.registrarPaquete();
                break;
            case 4:
                sistema.crearEnvio();
                break;
            case 5:
                sistema.agregarPaqueteAEnvio();
                break;
            case 6:
                sistema.mostrarEnvios();
                break;
            case 7:
                cout << "Saliendo del sistema..." << endl;
                break;
            default:
                cout << "Opción no válida. Intente de nuevo." << endl;
                break;
        }
    } while (opcion != 7);

    return 0;
}
