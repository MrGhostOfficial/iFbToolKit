<?php defined('BASEPATH') OR exit('No direct script access allowed');

/*
* Name      : Facebook Bot (fb-bot)
* Author      : MrGhostOfficial
* Version     : 1.1
* Update      : 06 June 2020
* Telegram    : https://t.me/Nethantara
* 
* Changing/removing the author's name will not make you a real programmer
* Please respect me for making this tool from the beginning. :)
*/

class App extends CI_Controller {
  /*
    @Base url
  */
  public $base_url = 'https://mbasic.facebook.com';
  /*
    @User agent
    @Ganti dgn user agent perangkat anda kalo bisa
  */
  public $user_agent = 'Chrome/36.0.1985.125';

  public $current_version = '1.1';
  public $next_version = '1.2';
  public $yellow = "\e[93m";
  public $cyan = "\e[96m";
  public $green = "\e[92m";
  public $red = "\e[91m";
  public $reset = "\e[0m";

  public function __construct()
  {
    parent::__construct();
    date_default_timezone_set('Asia/Jakarta');
    $this->climate = $this->configs->climate();
    $this->return_menu = & get_instance();
  }

  public function cek_session()
  {
    $this->cookies = $this->configs->load_cookies();
    if (!$this->cookies)
    {
      $this->auth->login();
      $this->cookies = $this->configs->load_cookies();
      $this->return_menu->menu();
    }
    else
    {
      $this->return_menu->menu();
    }
  }

  private function logout()
  {
    $input = $this->climate->br()->input("  Are you sure? [{$this->yellow}Y/n{$this->reset}]:");
    $input = $input->prompt();
    if (strtolower($input) == 'y')
    {
      unlink('logs/cookies.txt');
      $this->climate->br()->out('  Cookies successfully removed');
      sleep(3);
      $this->cek_session();
    }
    else
    {
      $this->climate->br()->out('  Canceled');
      sleep(3);
      $this->cek_session();
    }
  }

  private function see_cookies()
  {
    $this->configs->clear();
    $date = date('D M j G:i:s Y');
    echo sprintf($this->configs->banner(), $date, 'See Your FB Cookies');
    $this->climate->out('  +------------------------------------------------------+');
    $this->climate->br()->out('  Your cookies: '.$this->green.$this->cookies);
    $this->configs->back_menu();
  }

  private function _curl_version()
  {
    $response = file_get_contents('https://raw.githubusercontent.com/MrGhostOfficial/iFbToolKit/master/version.txt');
    if (trim($response) == $this->current_version)
    {
      return FALSE;
    }
    else if (trim($response) == $this->next_version)
    {
      return TRUE;
    }
    else
    {
      return FALSE;
    }
  }
 
  public function index()
  {
    $this->cek_session();
  }

  public function menu()
  {
    $this->configs->clear();
    $date = date('D M j G:i:s Y');
    echo sprintf($this->configs->banner(), $date, 'Checking cookies...');
    $version = $this->_curl_version();
    $response = $this->configs->request_get($this->base_url.'/profile.php', $this->cookies);
    if (strpos($response, 'mbasic_logout_button') === FALSE)
    {
      $this->configs->clear();
      $date = date('D M j G:i:s Y');
      echo sprintf($this->configs->banner(), $date, 'Invalid cookies');
      unlink('logs/cookies.txt');
      $this->climate->shout('  [WARNING] Cookies invalid please login again.');
      $input = $this->climate->br()->input('  Press enter');
      $input->prompt();
      $this->auth->login();
      return false;
    }
    $dom = new DOMDocument();
    @$dom->loadHTML($response);
    $name = $dom->getElementsByTagName('title');
    $name = $name->item(0)->nodeValue;
    $this->configs->clear();
    $date = date('D M j G:i:s Y');
    echo sprintf($this->configs->banner(), $date, $name);
    if ($version)
    {
      $this->climate->info("     New version is available. update your fb-bot now");
    }
    foreach ($this->configs->show_menu() as $menu)
    {
      $this->climate->out("    {$this->red}[{$this->yellow}{$menu->no}{$this->red}]{$this->reset}. $menu->name");
    }
    $input = $this->climate->br()->input("  Choice{$this->red}:");
    $input = $input->prompt();
    if (is_numeric($input) and isset($this->configs->show_menu()[$input-1]))
    {
      $title = $this->configs->show_menu()[$input-1]->name;
    }
    switch (strtolower($input))
    {
      case '01':
        $this->tools->chat_messages_eraser($title);
        break;
      case '02':
        $this->tools->post_eraser($title);
        break;
      case '03':
        $this->tools->friendslist_eraser($title);
        break;
      case '04':
        $this->tools->photo_album_eraser($title);
        break;
      case '05':
        $this->tools->friends_request($title);
        break;
      case '06':
        $this->tools->mass_join_groups($title);
        break;
      case '07':
        $this->tools->update_status($title);
        break;
      case '08':
        $this->tools->mass_chat($title);
        break;
      case '09':
        $this->tools->spam_chat($title);
        break;
      case '10':
        $this->tools->mass_leave_group($title);
        break;
      case '11':
        $this->tools->mass_react($title);
        break;
      case '12':
        $this->tools->mass_comments($title);
        break;
      case '13':
        $this->tools->spam_comments($title);
        break;
      case '14':
        $this->tools->mass_posting_groups($title);
        break;
      case '15':
        $this->tools->cancel_request_sent($title);
        break;
      case '16':
        $this->tools->unblock_user($title);
      case 'sc':
        $this->see_cookies();
        case 'rc':
        $this->logout();
        case 'ex':
        $this->climate->br()->yellow("  Bye don't forget to come back again:)");
        exit(0);
      default:
        $this->climate->br()->shout('  Wrong Input');
        sleep(3);
        $this->index();
        break;
    }
  }
}
