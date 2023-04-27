from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Группа деканата в ВК",
                                          url="https://vk.com/pb_fmiit"
                                      )
                                  ]
                              ])
