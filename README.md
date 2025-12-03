# Fast SNMP
*Fast SNMP* es un microservicio especializado en las consultas a los equipos bajo el protocolo SNMPv2. Diseñado para la fácil obtención de información de los distintos equipos en la red.

![](./docs/diagram.png)

---

**Tabla de Contenido**
- [Instalación](#Instalación)
  - [Requerimientos](#Requerimientos)
    - [Archivo de Configuración](#Archivo-de-Configuración)
  - [Entorno Virtual](#Entorno-Virtual)

---

# Instalación
## Requerimientos
Es necesario tener instalado Python 3.13 o superior.

### Archivo de Configuración
Este microservicio puede realizar las consulta SNMP de forma remota o de manera local. Para poder determinar este tipo de configuración, es necesario crear un archivo de configuración en formato JSON llamado `ssh.production.json` (o `ssh.development.json` si se trabaja en modo desarrollo) con la siguiente estructura:

```json
{
  "localConnection": "false",
  "credentials": [
    {
      "user": "user",
      "password": "password",
      "host": "127.0.0.1",
      "port": 22
    }
  ],
  "commandPing": "ping",
  "commandSNMP": "snmpwalk"
}
```

Si se especifica `localConnection` como `true`, el microservicio realizará las consultas SNMP de manera local. De lo contrario, se necesita especificar las credenciales de acceso a los equipos remotos. Si se especifican varias credenciales, el microservicio realizará un *SSH jump* para realizar las consultas en el último equipo de la lista.

## Entorno virtual
Este microservicio está diseñado para ser un paquete instalable en Python. Se recomienda activar un entorno virtual antes de instalarlo para evitar posibles conflictos con librerías existintes:
```bash
pip install fast-snmp
```
