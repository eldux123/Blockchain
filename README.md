# Blockchain en Python

Proyecto de clase para implementar una cadena de bloques simple usando Python.

## Funcionalidades

- Crea una cadena iniciando con un bloque genesis.
- Agrega bloques con informacion o transacciones.
- Calcula hashes SHA-256 para cada bloque.
- Usa prueba de trabajo con dificultad configurable.
- Guarda en cada bloque:
  - informacion
  - hash anterior
  - estampa de tiempo
  - dificultad
  - nonce
  - hash actual
- Permite consultar bloques por indice.
- Permite modificar bloques.
- Permite eliminar bloques.
- Verifica si la cadena completa es valida.
- Demuestra que modificar un bloque sin recalcular la cadena rompe su integridad.

## Ejecucion

```bash
python main.py
```

## Estructura

- `Block`: representa un bloque individual.
- `Blockchain`: administra la cadena, la mineria, la validacion y las operaciones
  de consulta, modificacion y eliminacion.
- `run_integrity_demo`: crea una cadena de ejemplo y muestra como cambia la
  validez al alterar bloques.

## Nota

Esta implementacion es educativa. No incluye red distribuida, billeteras,
firmas digitales ni consenso entre nodos.
