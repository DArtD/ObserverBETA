from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="SDO",
                                          url="https://sdo.bashedu.ru"
                                      ),
                                      InlineKeyboardButton(
                                          text="Личный кабинет",
                                          url="https://cabinet.bashedu.ru"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Заказать справку о доходах",
                                          url="https://isbashgu.bashedu.ru/uslugi/Default.aspx"
                                      ),
                                      InlineKeyboardButton(
                                          text="Заказать справку с места учебы",
                                          url="https://student-spravki.bashedu.ru/application_form"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Группа деканата в ВК",
                                          url="https://vk.com/pb_fmiit"
                                      ),
                                      InlineKeyboardButton(
                                          text="Группа УУНиТ в ВК",
                                          url="https://vk.com/uustufa"
                                      )
                                  ]
                              ])
