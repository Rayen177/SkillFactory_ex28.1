# SkillFactory_ex28.1
final Pagee Object project

для каждой рассмотренной страницы был создан свой файл, в котором описаны тесты.
некоторые тесты валятся по причине TimeoutException, во всех этих случаях это проблема 
из-за капчи, которую нужно ввести вручную. если во время выполнения теста успеть ввести код из 
капчи, тогда тест проходит.
Вобщем, именно капча мешает больше всего организовать тестирование сценариев от и до.
и еще одна глобальная проблема, это когда надо ввести код подтверждения из sms или письма на 
почту. в этих случаях, я делал тест до мемента отправки этих кодов, т.е. если я попал на 
страницу где я должен ввести полученый код, это уже свидетельствует о хорошем выполнении сценария.

надеюсь, что Вам понравится моя работа, много времени на нее потратил. но не смотря на то, что 
моих баллов хватает для финального теста, считаю, что работу по page object надо сдать обязательно.