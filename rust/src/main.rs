use std::io;

struct MyAI {
    // ...
}

enum LogType {
    Unknown,
    Error,
    Message,
    Debug,
}

impl LogType {
    fn to_str(&self) -> &str {
        match self {
            Self::Unknown => "UNKNOWN",
            Self::Error => "ERROR",
            Self::Message => "MESSAGE",
            Self::Debug => "DEBUG",
        }
    }
}

impl MyAI {
    fn new() -> Self {
        Self {
            // ...
        }
    }

    fn handle_about(&mut self, _cmd: &str) -> bool {
        let bot_name = "rust_template";
        println!("name=\"{bot_name}\", version\"0.42\"");
        false
    }

    fn handle_start(&mut self, cmd: &str) -> bool {
        todo!()
    }

    fn handle_end(&mut self, _cmd: &str) -> bool {
        true
    }

    fn handle_info(&mut self, cmd: &str) -> bool {
        todo!()
    }

    fn handle_begin(&mut self, cmd: &str) -> bool {
        todo!()
    }

    fn handle_turn(&mut self, cmd: &str) -> bool {
        todo!()
    }

    fn handle_board(&mut self, cmd: &str) -> bool {
        todo!()
    }

    fn send_log(&self, log_type: LogType, msg: &str) {
        let log_str = log_type.to_str();
        println!("{log_str}: {msg}");
    }

    fn handle_command(&mut self, cmd: &str) -> bool {
        let uppercase = cmd.split_whitespace().next().unwrap().to_uppercase();
        let token = uppercase.as_str();

        match token {
            "ABOUT" => self.handle_about(&cmd),
            "START" => self.handle_start(&cmd),
            "END" => self.handle_end(&cmd),
            "INFO" => self.handle_info(&cmd),
            "BEGIN" => self.handle_begin(&cmd),
            "TURN" => self.handle_turn(&cmd),
            "BOARD" => self.handle_board(&cmd),
            _ => {
                self.send_log(LogType::Unknown, "command not implemented");
                false
            }
        }
    }
}

fn main() -> std::io::Result<()> {
    let mut ai = MyAI::new();
    let mut input = String::new();

    loop {
        input.clear();
        let n = io::stdin().read_line(&mut input)?;

        if n == 0 {
            return Ok(());
        }

        if ai.handle_command(&input) {
            return Ok(());
        }
    }
}
