## Поиск в CSS
  по id = #id_name
  по class = .class_name
  по tag = div
  по значению атрибута = [attribute="value"]
  < !Важно. В современных JavaScript-фреймворках id-атрибуты чаще всего генерируются динамически самим фреймворком, поэтому они изменяются каждый раз при перезагрузке страницы и совершенно нечитабельны, например: вы увидите что-то вроде id="u_ps_0_0_n" или id="avadspffd". В таких случаях вам придется пользоваться другими селекторами или использовать собственные data-атрибуты. Названия классов также могут генерироваться автоматически. Поэтому предлагаем вам простое правило: если увидите нечеловекочитаемое значение атрибута или если значение атрибута меняется при перезагрузке страницы, то не используйте его. >
  ### Иерархия поиска в CSS
    Использование потомков = #id_name .child_class_name
    Использование дочерних элементов = #id_name > div.class_name
    Использование порядкового номера дочернего элемента = #id_name > .child_class_name:nth-child(2) > .grandchild_class_name
    Использование нескольких классов = .class_name.second_class_name

## с помощью XPath
  да ну его///

# Поиск в selenium
  ### find_element
    > возвращает только первый из всех элементов, которые подходят под условия поиск
  ### find_elements
    > список всех найденных элементов по заданному условию
    < !Важно. Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements. Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException, которая прервёт выполнение вашего кода. Второй же метод всегда возвращает валидный результат: если ничего не было найдено, то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде. >

## Типы поиска элементов
  ### (By.ID, value) 
    >— поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
  ### (By.CSS_SELECTOR, value)
    >— поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
  ### (By.XPATH, value)
    >— поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
  ### (By.NAME, value)
    >— поиск по атрибуту name элемента;
  ### (By.TAG_NAME, value)
    >— поиск элемента по названию тега элемента;
  ### (By.CLASS_NAME, value)
    >— поиск по значению атрибута class;
  ### (By.LINK_TEXT, value)
    >— поиск ссылки на странице по полному совпадению;
  ### (By.PARTIAL_LINK_TEXT, value)
    >— поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

# Работа с элементами
  ## Взаимодействие
  ### click()
    >- осуществить клик по элементу
  ### send_keys(value)
    >- вписать значение value в поле
  ### get_attribute(value)
    >- достать значение атрибута с именем value из элемента
  ### element_name.text
    >- достать текст из элемента
  ### element_name.select_by_value(value)
    >- Найти элемент из списка по значению (только для списков)
  ### element_name.select_by_visible_text(value)
    >- Найти элемент из списка по отображаемому тексту (только для списков)
  ### element_name.select_by_index(index)
    >- Найти элемент из списка по индексу (только для списков)
###

###

  ## Методы WebDriver
  ### browser.switch_to.window(window_name)
  > переключиться на вкладку с именем window_name
  ### browser.window_handles[index]
  > узнать имя вкладки
  ### browser.execute_script("js script")
    >- выполнить скрипт на языке js
  ### browser.implicitly_wait(num_seconds)
    >- настроить ожидание для отработки теста в num_seconds секунд
  ## browser.switch_to.alert
    >- выбрать окно
  ### element_window.accept()
    >- клик "ОК" в окне
  ### element_window.dismiss()
    >- клик "Отмена" в окне