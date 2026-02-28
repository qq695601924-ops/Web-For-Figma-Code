export interface FaqItem {
  title: string
  content: string
}

export const faqList: FaqItem[] = [
  {
    title: '¿Monto de préstamo?',
    content: 'GiroFácil ofrece préstamos con un monto máximo de 30,000 pesos, cuyo crédito exacto es evaluado por el sistema según la información proporcionada en su solicitud.',
  },
  {
    title: '¿Cómo solicitar un préstamo?',
    content: 'Desde Google Play Store puede descargar GiroFácil, regístrese con su número celular e inicie sesión para solicitar un préstamo.',
  },
  {
    title: '¿Cómo obtener el monto del préstamo?',
    content: 'Inicie sesión en la aplicación. Después de ingresar la información personal solicitada de acuerdo al proceso, evaluaremos su solicitud después de completarla. Esto determinará si se le concederá una línea de crédito. Para asegurarse de obtener el monto del préstamo sin problemas, le recomendamos verificar la vigencia de toda su información.',
  },
  {
    title: 'Cometí un error al completar mi perfil, ¿puedo modificar mi perfil?',
    content: 'Para la conservación y protección de datos personales, después de la presentación exitosa de sus datos no se admite la modificación. Verifica cuidadosamente la información ingresada antes de enviar.',
  },
  {
    title: '¿Cuánto tiempo dura el proceso de aprobación del préstamo?',
    content: `1. Después de rellenar todos sus datos personales, la mayoría de las aprobaciones de los créditos de los préstamos se procesarán en 3 minutos.
2. La mayoría de las aprobaciones del depósito del préstamo se completan en 1-2 horas, con un máximo de 24 horas. Si no ha recibido su préstamo después de 24 horas, póngase en contacto con servicio de atención al cliente.`,
  },
  {
    title: '¿Como recibir mi préstamo?',
    content: 'Si su solicitud está aprobada, normalmente el depósito se tardará unas 2-3 horas en llegar con éxito a su cuenta. Las transferencias bancarias pueden retrasarse debido a problemas de la red del sistema, así que no se preocupe demasiado. Si el pago es exitoso, GiroFácil le enviará una notificación, así que sea paciente. GiroFácil solo empezará a calcular los intereses a partir del día siguiente a la realización del depósito. Si no ha recibido el depósito más de 24 horas, póngase en contacto con el servicio de atención al cliente.',
  },
  {
    title: '¿Se puede aumentar el monto del préstamo?',
    content: 'GiroFácil evalúa regularmente el crédito del usuario de forma razonable y le ofrece un límite de préstamo adecuado a su solvencia. Le recomendamos que mantenga un buen crédito de préstamo haciendo sus pagos a tiempo, ya que repetir un buen crédito le ayudará a obtener un crédito de préstamo más alto.',
  },
  {
    title: 'Si mi solicitud de préstamo no fue aprobada, ¿puedo volver a solicitarla?',
    content: 'Si su solicitud de préstamo no es aprobada, significa que en este momento no cumple con los requisitos para solicitar un préstamo en GiroFácil. Se le enviará una notificación cuando cumpla con los requisitos de la solicitud y podrá volver a aplicar.',
  },
  {
    title: '¿Puedo cancelar mi solicitud de préstamo?',
    content: 'Una vez enviada la solicitud de préstamo, se procesará automáticamente y no se podrá cancelar. Si tiene alguna duda, comuníquese con el servicio de atención al cliente.',
  },
]
