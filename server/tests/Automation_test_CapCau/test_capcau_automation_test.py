from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.Generated.Tests.MyFirstProject
    Test: Capcau_Automation_test
    Generated by: Khắc Hùng - Ca hát thật đơn giản (thaiembinh14@gmail.com)
    Generated on 05/01/2022, 13:15:55
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="hC2UsG-j4g-MsgLpq6sIM93vqWQLQ-26gvs_tS7Mi40",
                              project_name="My first Project",
                              job_name="Capcau_Automation_test")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "http://localhost:3005/sentence"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'username'
    username = driver.find_element(By.CSS_SELECTOR,
                                   "#username")
    username.click()

    # 3. Type 'admin' in 'username'
    username = driver.find_element(By.CSS_SELECTOR,
                                   "#username")
    username.send_keys("admin")

    # 4. Click 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.click()

    # 5. Type '12345678' in 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.send_keys("12345678")

    # 6. Click 'Đăng nhập'
    _ng_nh_p = driver.find_element(By.XPATH,
                                   "//button[. = 'Đăng nhập']")
    _ng_nh_p.click()

    # 7. Click 'Tìm kiếm câu...'
    t_m_ki_m_c_u_ = driver.find_element(By.XPATH,
                                        "//input[@placeholder = 'Tìm kiếm câu...']")
    t_m_ki_m_c_u_.click()

    # 8. Type 'Alo' in 'Tìm kiếm câu...'
    t_m_ki_m_c_u_ = driver.find_element(By.XPATH,
                                        "//input[@placeholder = 'Tìm kiếm câu...']")
    t_m_ki_m_c_u_.send_keys("Alo")

    # 9. Click 'Chưa đánh giá'
    ch_a_nh_gi_ = driver.find_element(By.XPATH,
                                      "//span[. = 'Chưa đánh giá']")
    ch_a_nh_gi_.click()

    # 10. Click 'Chưa đánh giá'
    ch_a_nh_gi_ = driver.find_element(By.XPATH,
                                      "//span[. = 'Chưa đánh giá']")
    ch_a_nh_gi_.click()

    # 11. Click 'Tốt'
    t_t = driver.find_element(By.XPATH,
                              "//div[2]/div[. = 'Tốt']")
    t_t.click()

    # 12. Type '-1' in 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.send_keys("-1")

    # 13. Click 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.click()

    # 14. Type '0' in 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.send_keys("0")

    # 15. Click 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.click()

    # 16. Type '1' in 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.send_keys("1")

    # 17. Click 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.click()

    # 18. Type '2' in 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.send_keys("2")

    # 19. Click 'Từ'
    t_ = driver.find_element(By.XPATH,
                             "//input[@placeholder = 'Từ']")
    t_.click()

    # 20. Click 'Ngày bắt đầu'
    ng_y_b_t_u = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Ngày bắt đầu']")
    ng_y_b_t_u.click()

    # 21. Click '12'
    _12 = driver.find_element(By.XPATH,
                              "//td[4]/div[. = '12']")
    _12.click()

    # 22. Click 'Ngày kết thúc'
    ng_y_k_t_th_c = driver.find_element(By.XPATH,
                                        "//input[@placeholder = 'Ngày kết thúc']")
    ng_y_k_t_th_c.click()

    # 23. Click 'Ngày bắt đầu'
    ng_y_b_t_u = driver.find_element(By.XPATH,
                                     "//input[@placeholder = 'Ngày bắt đầu']")
    ng_y_b_t_u.click()

    # 24. Click '4'
    _4 = driver.find_element(By.XPATH,
                             "//td[3]/div[. = '4']")
    _4.click()

    # 25. Click 'Ngày kết thúc'
    ng_y_k_t_th_c = driver.find_element(By.XPATH,
                                        "//input[@placeholder = 'Ngày kết thúc']")
    ng_y_k_t_th_c.click()

    # 26. Click '14'
    _14 = driver.find_element(By.XPATH,
                              "//td[6]/div[. = '14']")
    _14.click()

    # 27. Click 'Nhập tên người dùng...'
    nh_p_t_n_ng_i_d_ng_ = driver.find_element(By.XPATH,
                                              "//div[1]/div/div[. = 'Nhập tên người dùng...']")
    nh_p_t_n_ng_i_d_ng_.click()

    # 28. Type '[NONE]' in 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//div[2]/input")
    input.send_keys("")

    # 29. Click 'Nhập tên người dùng...'
    nh_p_t_n_ng_i_d_ng_ = driver.find_element(By.XPATH,
                                              "//div[1]/div/div[. = 'Nhập tên người dùng...']")
    nh_p_t_n_ng_i_d_ng_.click()

    # 30. Click 'user_97'
    user_97 = driver.find_element(By.XPATH,
                                  "//div[. = 'user_97']")
    user_97.click()

    # 31. Click 'Tất cả'
    t_t_c_ = driver.find_element(By.XPATH,
                                 "//span[. = 'Tất cả']")
    t_t_c_.click()

    # 32. Click 'Tiếng Việt'
    ti_ng_vi_t = driver.find_element(By.XPATH,
                                     "//div[2]/div[. = 'Tiếng Việt']")
    ti_ng_vi_t.click()

    # 33. Click 'Tìm kiếm'
    t_m_ki_m = driver.find_element(By.XPATH,
                                   "//span[. = 'Tìm kiếm']")
    t_m_ki_m.click()

    # 34. Click 'Tiếng Việt1'
    ti_ng_vi_t1 = driver.find_element(By.XPATH,
                                      "//th[4][. = 'Tiếng Việt']")
    ti_ng_vi_t1.click()

    # 35. Click 'svg'
    svg = driver.find_element(By.XPATH,
                              "//th[5]/div/div/span[2]/span/span[2]/*")
    svg.click()

    # 36. Click 'DIV'
    div = driver.find_element(By.XPATH,
                              "//th[5]/div/div")
    div.click()

    # 37. Click 'Ngày cập nhật'
    ng_y_c_p_nh_t = driver.find_element(By.XPATH,
                                        "//span[. = 'Ngày cập nhật']")
    ng_y_c_p_nh_t.click()

    # 38. Scroll window by ('0','22')
    driver.execute_script("window.scrollBy(0,22)")

    # 39. Scroll window by ('0','-22')
    driver.execute_script("window.scrollBy(0,-22)")

    # 40. Click 'Thống kê'
    th_ng_k_ = driver.find_element(By.XPATH,
                                   "//button[. = 'Thống kê']")
    th_ng_k_.click()

    # 41. Scroll window by ('0','212')
    driver.execute_script("window.scrollBy(0,212)")

    # 42. Scroll window by ('0','15')
    driver.execute_script("window.scrollBy(0,15)")

    # 43. Scroll window by ('0','270')
    driver.execute_script("window.scrollBy(0,270)")

    # 44. Scroll window by ('0','-265')
    driver.execute_script("window.scrollBy(0,-265)")

    # 45. Scroll window by ('0','-232')
    driver.execute_script("window.scrollBy(0,-232)")