## Введение

Объект представляет из себя совокупность:
- поведения (behavior) - набор операций, методов
- состояния (state) - набор значений
при этом переход из одного состояния в другое происходит за счет выполнения операций

Сигнатура - это имя операция, параметры и возвращаемое значение

Интерфейс объекта - множество сигнатур операций объекта (без реализации) - публично доступные методы  

Тип - это именованный интерфейс

Динамическое связывание - определение реализации в рантайме - в момент исполнения 
Какой код будет выполняться - то проявление полиморфизма

Постановка задачи -> Выделение сущностей, абстрагирование -> Построение модели 

Нужно находить баланс между детализированным и слишком обобщенным объектом - в данном вопросе помогают шаблоны 

Инстанциирование, создание экземпляра - создание объекта на основе класса 
Абстрактные классы - содержащие операции без реализации. Есть также конкретные

Тип - это именованный интерфейс. Класс - это реализация типа

Нужно стараться разрабатывать, используя интерфейсы, а не классы

Святой грааль - это повторное использование кода:
- наследование 
- композиция 

#### Наследование

whitebox - класс-наследник видит все операции родителя
определяется статически на этапе компиляции
по сути нарушает инкапсуляцию
Сильная связь изменение родителя скорее всего приводит к изменению наследников - можно частично решить за счет абстрактных классов

#### Композиция

blackbox - доступны только открытые методы других объектов
определяется динамически во время выполнения 
Можно применить, если объекты соблюдают интерфейсы друг друга 
Объекты не разрастаются, происходит делегирование функционала


Следует предпочитать композицию наследованию! 


## Порождающие паттерны (Creational)

Абстрагируют процесс инстанциирования 
Инкапсулируют знания о конкретных классах
Скрывают детали того, как классы создаются и стыкуются

### Фабричный метод (Virtual Constructor)

Определяет интерфейс создания объекта, но оставляем подклассам решение, какой класс инстанциировать - класс делегирует подклассам инстанциирование  
Отделяет код создания продуктов от остального кода, который использует эти продукты
Делает код более гибким
Позволяет создавать в классах hook (зацепки) для предоставления расширенной версии объекта

### Абстрактная фабрика (Kit)

Позволяет создавать семейства связанных объектов, не привязываясь к конкретным классам
Изолирует конкретные классы
Упрощает замену семейств продуктов
Гарантирует сочетаемость продуктов
Поддерживать новый вид продуктов трудно 

По сути является набором связанных фабричных методов

### Строитель (Builder) 

Отделяет конструирование сложного объекта от его представления
Конструирование объекта осуществляется внешними сущностями - строителями
Позволяет избавиться от конструктора со множеством опциональных параметров

Сам строитель обеспечивает набор функционала, а директор уже обладает знанием в какой последовательности и с какими параметрами вызывать методы строителя


### Прототип (Prototype)

Задает виды создаваемых объектов с помощью экземпляра-прототипа, создает объекты путем его копирования
Предлагает использовать набор прототипов вместо создания подклассов
Основной недостаток - то, что каждый подкласс класс Prototype должен реализовывать функцию Clone


### Синглтон (Singleton)

Гарантирует, что у класса есть только один экземпляр и предоставляет к нему глобальную точку доступа




## Структурные паттерны (Structural)

Образуют из классов и объектов более крупные структуры
Структурные паттерны уровня класса - используют наследование для составления композиций из интерфейсов и реализаций
Структурные паттерны уровня объектов - компонуют объекты для получения новой функциональности

### Адаптер (Adapter) - Обертка (Wrapper)

Главная задача - решить проблему несовместимости интерфейсов
Два варианта
1. 
2. 

### Мост (Bridge)

Позволяет разделить две иерархии - абстракции и реализации

**Bridge** разделяет абстракцию и реализацию **на этапе проектирования**
**Adapter** совмещает **уже существующие** несовместимые интерфейсы.

Паттерн Bridge полезен, когда:

- Система должна работать с **разными типами абстракций и реализаций**.
- Вы хотите **избежать наследования** в пользу гибкой композиции.



### Компоновщик (Composite)

Компонует объекты в древовидные структуры для представления иерархий часть-целое

**Главный принцип:**

> _"Одинаковый интерфейс для листьев и составных объектов."_



### Декоратор (Decorator)

Позволяет динамически добавлять объекту новые возможности
Использует композицию вместо наследования


### Фасад (Facade)

Предоставляет унифицированный интерфейс вместо набора интерфейсов некоторой подсистемы

✅ **Плюсы**:

- Упрощает работу со сложными системами.
- Уменьшает связанность кода.
- Позволяет легко заменить подсистему (достаточно изменить фасад).
❌ **Минусы**:
- Фасад может стать **"божественным объектом"**, если взять на себя слишком много.
- Дополнительный срос абстракции (иногда избыточный для простых задач).

Примеры:
- ORM (например, Django ORM — фасад для работы с БД).
- Библиотеки типа `requests` (упрощают HTTP-запросы).


### Кэш (Flyweight)

Предназначен для экономии оперативной памяти 

✅ **Плюсы**:

- Экономит **оперативную память**.
- Уменьшает количество создаваемых объектов.

❌ **Минусы**:

- Усложняет код из-за разделения состояния.
- Неэффективен, если внешних данных больше, чем внутренних.


### Прокси (Proxy)

**Паттерн Proxy** предоставляет **объект-заместитель**, который контролирует доступ к другому объекту, добавляя дополнительную логику (например, ленивую загрузку, кеширование, проверку доступа)

Декоратор - **Динамически добавляет** новое поведение объекту, **расширяя** его функциональность. Прокси -  **Контролирует доступ** к объекту, **не меняя его основную логику** (ленивая загрузка, защита, кеширование).

**Типы прокси**
1. **Виртуальный прокси** — откладывает создание объекта.
2. **Защитный прокси** — контролирует доступ.
3. **Удаленный прокси** — представляет объект в другом адресном пространстве.  
4. **Кеширующий прокси** — сохраняет результаты запросов.

✅ **Плюсы**:
- Контроль доступа к объекту.
- Ленивая инициализация и кеширование.
- Упрощение работы с ресурсоемкими объектами.

❌ **Минусы**:
- Усложнение кода.
- Дополнительные накладные расходы.


Примеры:
- ORM (ленивая загрузка полей объекта из БД).
- `@property` в Python (контроль доступа к атрибутам).

## Поведенческие паттерны (Behavioral)

### Цепочка обязанностей (Chain of responsibility)

Позволяет передавать запрос по цепочке обработчиков. Каждый обработчик решает, может ли он обработать запрос, или передает его следующему в цепочке.

- Когда нужно **динамически определять**, какой объект должен обработать запрос.
- Когда **несколько объектов** могут обработать запрос, но выбор обработчика зависит от типа запроса.
- Когда важно **разделять отправителя и получателя** запроса.

✅ **Плюсы**:
- Уменьшает зависимость между отправителем и получателем.
- Гибкость: можно динамически менять цепочку.
- Упрощает добавление новых обработчиков.

❌ **Минусы**:
- Запрос может остаться необработанным (если ни один обработчик не подходит).
- Цепочка может усложнить отладку.

Примеры:
- Middleware в Django/Flask.
- Фильтрация событий в GUI (например, обработка кликов).
- Логирование и аудит в корпоративных приложениях.


### Наблюдатель (Observer)

**Паттерн Observer** позволяет объектам (**наблюдателям**) подписываться на события другого объекта (**субъекта**) и автоматически получать уведомления при изменении его состояния. Это основа **событийно-ориентированной 
архитектуры**.

В Python его можно реализовать:
1. Через **абстрактные классы** (как в примерах выше).
2. С помощью **слотов событий** (`signals` в PyQt).
3. Через **декораторы** или **коллбэки**.

✅ **Плюсы**:
- Гибкая связь между объектами (**издатель не знает о подписчиках**).
- Легко добавлять новых наблюдателей.
- Реализует **принцип открытости/закрытости**.

❌ **Минусы**:
- Подписчики **могут получать ненужные уведомления**.
- Возможны **утечки памяти**, если не отписываться от субъекта.



### Итератор (Iterator)

**Паттерн Iterator** предоставляет способ последовательного доступа к элементам коллекции **без раскрытия её внутренней структуры**. В Python это встроенный механизм, реализуемый через протокол итераторов.


✅ **Плюсы**:
- Упрощает **обход сложных структур данных**.
- Позволяет **лениво вычислять элементы** (генераторы).
- Скрывает **детали реализации коллекции**.
❌ **Минусы**:
- В некоторых случаях менее эффективен, чем прямой доступ к элементам.
- Одноразовый: после завершения итерации нужно создавать новый итератор.

- В Python итераторы **встроены в язык** (через `iter()` и `next()`).
- Для создания своих итераторов реализуйте `__iter__()` и `__next__()`.
- **Генераторы** — это удобный способ создания итераторов



### Команда (Command)

**Паттерн Command** инкапсулирует запрос в виде объекта, позволяя параметризовать клиенты с различными запросами, ставить их в очередь или логировать. Он отделяет _отправителя_ команды от её _исполнителя_.

- Когда нужно **отделить инициацию операции** от её выполнения.
- Для реализации **отмены операций** (undo/redo).
- Для **очереди команд** или их логирования.
- В GUI для обработки действий (кнопки, меню)

✅ **Плюсы**:
- Убирает прямую зависимость между инициатором и получателем.
- Позволяет реализовать **отмену операций**, **очереди команд**, **логирование**.
- Упрощает добавление новых команд.
❌ **Минусы**:
- Увеличивает количество классов.
- Может усложнить код для простых задач

В Python часто реализуется через **классы** или **функции как объекты** (с `__call__`).


### Посредник (Mediator, Controller)

**Паттерн Mediator** позволяет уменьшить связанность множества классов между собой, перенося их взаимодействие в единый класс-посредник. Вместо прямого общения объекты взаимодействуют через централизованный компонент.

- Когда много объектов общаются друг с другом сложным образом.
- Когда нужно упростить взаимодействие между компонентами системы.
- Для управления состоянием системы через единую точку контроля.

✅ **Плюсы**:
- Уменьшает связанность между компонентами.
- Централизует управление взаимодействиями.
- Упрощает добавление новых участников.
❌ **Минусы**:
- Посредник может стать **"божественным объектом"** (слишком сложным).
- Увеличивает количество классов.

Медиатор управляет взаимодействием множества объектов через посредника. Фасад же упрощает интерфейс к сложной подсистеме (но не управляет связями).


### Хранитель (Memento)

**Паттерн Memento** позволяет сохранять и восстанавливать предыдущие состояния объекта, не раскрывая деталей его реализации. Это полезно для реализации функционала **отмены действий (undo)**, **сохранения истории изменений** или **снимков состояния системы**.

✅ **Плюсы**:
- Сохраняет инкапсуляцию объекта.
- Упрощает реализацию отмены операций.
- Позволяет хранить историю состояний.
❌ **Минусы**:
- Может потреблять много памяти, если состояний много.
- Усложняет код, если объектов много.



### Состояние (State)

**Паттерн State** позволяет объекту **изменять свое поведение** при изменении его внутреннего состояния. Внешне это выглядит так, будто объект **изменил класс**.

- Когда поведение объекта зависит от его состояния, и оно должно изменяться во время выполнения.
- Когда в коде много условных операторов (`if-else` или `switch`), которые проверяют состояние объекта.
- Когда у вас есть множество состояний, и вы хотите сделать код более читаемым и поддерживаемым.

✅ **Плюсы**:
- Избавляет от множества `if-else` условий.
- Упрощает добавление новых состояний.
- Делает код более читаемым и поддерживаемым.
❌ **Минусы**:
- Может быть избыточным, если состояний мало.
- Увеличивает количество классов.


### Стратегия (Strategy)

**Паттерн Strategy** позволяет определить семейство алгоритмов, инкапсулировать каждый из них и делать их взаимозаменяемыми. Он позволяет изменять алгоритмы независимо от клиента, который их использует.

✅ **Плюсы**:
- Замена алгоритмов **на лету**.
- Избегание **условных операторов**.
- Инкапсуляция **алгоритмов** в отдельные классы.
❌ **Минусы**:
- Увеличивает **количество классов**.
- Клиент должен **знать о стратегиях**

Примеры:
- Оплата (кредитные карты, PayPal, криптовалюта).
- Сортировка (пузырьком, быстрая, слиянием).
- Генерация отчетов (JSON, CSV, HTML).



### Шаблонный метод (Template method)

**Паттерн Template Method** определяет **"скелет" алгоритма** в базовом классе, позволяя подклассам переопределять отдельные шаги, не меняя структуру алгоритма. Это позволяет избежать дублирования кода и стандартизировать поведение.

- Когда несколько классов выполняют **одинаковые шаги**, но с разной реализацией.
- Когда нужно **контролировать структуру алгоритма**, но разрешить гибкость в деталях.
- Для вынесения общего поведения в родительский класс.

✅ **Плюсы**:
- Исключает дублирование кода.
- Облегчает поддержку (изменения вносятся в одном месте).
- Контролирует структуру алгоритма.
❌ **Минусы**:
- Может ограничивать гибкость (если нужно менять порядок шагов).
- Усложняет иерархию классов.


Сравнение с другими паттернами

| Паттерн             | Цель                                                                  |
| ------------------- | --------------------------------------------------------------------- |
| **Template Method** | Определяет скелет алгоритма, позволяя подклассам переопределять шаги. |
| **Strategy**        | Инкапсулирует алгоритмы в отдельные классы для взаимозамены.          |
| **Factory Method**  | Делегирует создание объектов подклассам.                              |

**Шаблонный метод** идеален для:
- Стандартизации **последовательности операций**.
- Реализации **инвариантных частей алгоритма**.
- Примеры: игровые циклы, отчеты, приготовление еды.
**Главное преимущество**:
> _"Разделяй общее и изменяемое — сохраняй порядок, но разрешай гибкость."_




### Посетитель (Visitor)

**Паттерн Visitor** позволяет добавлять новые операции к объектам, **не изменяя их классы**. Он разделяет алгоритмы и структуры данных, что особенно полезно для сложных объектов (например, деревьев или AST).

- Когда нужно **добавить новые операции** к объектам, **не меняя их код**.
- Для обработки **сложных структур** (XML, AST, UI-компоненты).
- Когда операции должны **работать с разными классами объектов**.


✅ **Плюсы**:
- Добавляет новые операции **без изменения классов**.
- Объединяет родственные операции в одном классе `Visitor`.
- Упрощает добавление операций для **сложных структур**.
❌ **Минусы**:
- Нарушает инкапсуляцию (требует `public` методов для `Visitor`).
- Усложняет код, если **классы объектов часто меняются**.


Примеры:
- Обход DOM-дерева в браузерах.
- Генерация кода в компиляторах.
- Посетители в ORM (например, SQL-генерация).


