use std::time::Duration;

use criterion::{BenchmarkGroup, measurement::Measurement};

pub(crate) struct BenchmarkOptions {
    pub(crate) warm_up_time: Option<Duration>,
    pub(crate) measurement_time: Option<Duration>   
}

impl BenchmarkOptions {
    pub(crate) fn apply_to<'a, M: Measurement>(&self, group: &mut BenchmarkGroup<'a, M>) {
        if let Some(duration) = self.warm_up_time {
            group.warm_up_time(duration);
        }
        if let Some(duration) = self.measurement_time {
            group.measurement_time(duration);
        }
    }
}